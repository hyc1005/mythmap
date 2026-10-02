import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from backend.app.main import app, parse_bbox, place_list_filters, story_list_filters

client = TestClient(app)


def test_api_returns_422_for_invalid_theme_and_bbox_without_querying_database():
    assert client.get("/api/stories", params={"theme": "未知主题"}).status_code == 422
    assert client.get("/api/map/features", params={"bbox": "200,0,201,1"}).status_code == 422


def test_bbox_accepts_valid_extent_and_rejects_invalid_values():
    assert parse_bbox("70,15,140,55") == (70.0, 15.0, 140.0, 55.0)
    for value in ("1,2,3", "181,0,182,1", "10,5,9,6", "a,0,1,1"):
        with pytest.raises(HTTPException) as exc:
            parse_bbox(value)
        assert exc.value.status_code == 422


def test_story_filters_use_associations_and_validate_vocabulary():
    where, params = story_list_filters("  精卫  ", "神话事件", "person-1", "place-1", "clear")
    assert "story_people" in where and "story_places" in where
    assert params == {
        "q": "%精卫%", "theme": "神话事件", "person_id": "person-1",
        "place_id": "place-1", "confidence": "clear",
    }
    with pytest.raises(HTTPException) as exc:
        story_list_filters(None, "无效主题", None, None, None)
    assert exc.value.status_code == 422


def test_place_filters_include_unlocated_by_default_and_share_story_theme_semantics():
    where, params = place_list_filters(None, "山川地理", "story-1", None, "clear", True)
    assert "EXISTS (SELECT 1 FROM story_places" in where
    assert "fs.theme=:theme" in where and "sp.story_id=:story_id" in where
    assert "p.confidence <> 'unlocated'" not in where
    assert params == {"confidence": "clear", "story_id": "story-1", "theme": "山川地理"}
    where, _ = place_list_filters(None, None, None, None, None, False)
    assert "p.confidence <> 'unlocated'" in where


def test_place_search_combines_linked_story_and_person_constraints():
    where, params = place_list_filters("精卫", "神话事件", None, "person-1", None, True)
    assert "qs.title ILIKE :q" in where
    assert "qpp.person_id=:person_id" in where
    assert "fs.theme=:theme" in where
    assert params == {"theme": "神话事件", "person_id": "person-1", "q": "%精卫%"}

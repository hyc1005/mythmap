from fastapi import HTTPException

THEMES = ("山川地理", "神祇", "异兽", "方国", "神话事件")
CONFIDENCES = ("clear", "disputed", "unlocated")


def validate_theme(value: str | None) -> str | None:
    if value is not None and value not in THEMES:
        raise HTTPException(status_code=422, detail=f"theme must be one of: {', '.join(THEMES)}")
    return value


def validate_confidence(value: str | None) -> str | None:
    if value is not None and value not in CONFIDENCES:
        raise HTTPException(status_code=422, detail="confidence must be clear, disputed, or unlocated")
    return value

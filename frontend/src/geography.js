import associations from './geography-associations.json' with { type: 'json' };

export function validReference(record) {
  const coordinates = record.geometry?.coordinates;
  return record.geometry?.type === 'Point' && Array.isArray(coordinates) && coordinates.length === 2
    && coordinates.every(Number.isFinite) && Math.abs(coordinates[0]) <= 180 && Math.abs(coordinates[1]) <= 90
    && record.properties?.verification_status === 'modern_reference_verified';
}

export function referenceCollection(records) {
  return { type: 'FeatureCollection', name: 'Event traditions and geographic hypotheses; not established historical sites',
    features: records.filter(validReference).map(record => ({ ...record, properties: { ...record.properties, reference_only: true } })) };
}

export function groupReferences(records) {
  const groups = new Map();
  for (const record of records) {
    const key = record.geometry.coordinates.join(',');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(record);
  }
  return [...groups.values()];
}

export function unlocatedStories(catalog, chapter = '') {
  return geographicEvents(catalog).filter(event => (!chapter || event.properties.stage_id === chapter)
    && !geographicReferences(catalog).some(item => validReference(item) && item.properties.entity_id === event.id));
}

export function geographicEvents(catalog) {
  return catalog.stages.flatMap(stage => {
    const order = stage.event_ids || [];
    return catalog.events.filter(event => event.properties.stage_id === stage.id && !['archive', 'group'].includes(event.properties.presentation))
      .sort((a, b) => (order.includes(a.id) ? order.indexOf(a.id) : 999) - (order.includes(b.id) ? order.indexOf(b.id) : 999));
  });
}

export function defaultGeographicEvent(catalog, chapterId, currentEventId) {
  const events = geographicEvents(catalog);
  return events.find(event => event.id === currentEventId && event.properties.stage_id === chapterId)?.id
    || events.find(event => event.properties.stage_id === chapterId)?.id || events[0]?.id || '';
}

export function geographicReferences(catalog) {
  return [...catalog.candidates.map(record => ({ ...record, properties: {
    ...record.properties, association_type: 'research_hypothesis', location_precision: 'region_representative',
    evidence_status: 'pending', evidence: [], ...associations.evidence_updates[record.id],
  } })), ...associations.features].filter(validReference);
}

export const associationLabel = record => record.properties.association_type === 'local_tradition' ? '地方传说' : '地理考证';

const narratives = {
  '01-01-tradition-tongbai': ['天地初分，盘古的身体化入山川。桐柏的讲述把他的血液与淮水相连，开天旧说，便与一条河的来处相接。', 'Heaven and earth part, and Pangu’s body becomes the landscape. Tongbai’s account links his blood with the Huai: the beginning of the world meets the beginning of a river.'],
  '01-01-tradition-biyang': ['混沌分开，天地初定。盘古的名字，留在泌阳一座山的名字里；当地传说，把开天与居住的往事寄于此山。', 'Chaos opens; heaven and earth settle. Pangu’s name remains in a mountain in Biyang, where local tradition places his creation and dwelling.'],
  '03-04-tradition-changzi': ['精卫衔着西山的木石，往返山海。长子的讲述将西山认作发鸠山，又以灵湫庙寄托炎帝对女娃的思念。', 'Jingwei carries wood and stones between mountain and sea. Changzi’s account names the mountain Fajiu and links Lingqiu Temple with the Flame Emperor’s remembrance of his daughter.'],
  '03-04-tradition-gaoping': ['小鸟衔来木石，仍向东海飞去。高平寺庄的发鸠山，也承载着精卫的传说。', 'A small bird carries wood and stones toward the Eastern Sea. Mount Fajiu in Sizhuang, Gaoping, also carries Jingwei’s story.'],
  '03-01': ['阪泉的故事里，轩辕与炎帝相遇于兵戈之间。三次交战之后，胜负才定。', 'At Banquan, Xuanyuan and the Flame Emperor meet in battle. Only after three encounters is the outcome decided.'],
  '03-02': ['蚩尤不服帝命，黄帝于是会合诸侯，在涿鹿与他交战。古书所记，这一战以蚩尤被擒杀而终。', 'Chiyou defies imperial authority. The Yellow Emperor gathers the lords and meets him at Zhuolu. In the old account, the battle ends with Chiyou’s capture and death.'],
  '03-04': ['女娃在东海溺亡，化作精卫。她衔来西山的木石，要填平那片海；山海之间，小鸟往返。', 'Nüwa, the Flame Emperor’s daughter, drowns in the Eastern Sea and becomes Jingwei. She carries wood and stones from the western mountains to fill the sea, returning again and again.'],
  '04-04': ['洪水漫过大地，鲧取来能够生长的息壤，想替人间堵住水患。未经帝命，他最终在羽郊受诛。古书接着记下，鲧又生出禹。', 'Floodwater spreads across the land. Gun takes the self-growing soil xirang to hold it back. Acting without permission, he is put to death at Yujiao. The old account continues with Yu’s birth from Gun.'],
  '04-05': ['尧将天命交到舜手中，叮嘱他秉持中正，不让百姓陷入困穷。后来，舜又把这番话交给禹。', 'Yao entrusts heaven’s mandate to Shun, asking him to govern fairly and keep the people from hardship. Later, Shun passes the same words to Yu.'],
  '05-03': ['禹在涂山成婚，仍奔忙于水土之间。启出生啼哭时，他未能亲自照料。', 'Yu marries at Tushan, but his work on the land continues. When the infant Qi cries, Yu is still occupied elsewhere.'],
  '05-04': ['鼓声意外响起，送饭的涂山氏循声而来，见到的却是化作熊形的禹。她羞惭离去，身化为石；后来石头裂开，启从其中出生。', 'A drum sounds by accident. Yu’s wife comes with food and finds him in the form of a bear. She retreats in shame and turns to stone; later the stone splits and Qi is born.'],
  '06-01': ['夏政衰微，后羿从鉏迁往穷石，凭夏人的支持，接掌夏政。', 'As Xia weakens, Houyi moves from Chu to Qiongshi and takes power with the Xia people’s support.'],
  '06-02': ['后羿把信任交给寒浞，自己仍往来于田猎之间。寒浞以收买与欺骗积聚势力。后羿归来时，被家众所杀。', 'Houyi trusts Han Zhuo and continues his hunting. Han Zhuo gathers power through bribery and deceit. On his return, Houyi is killed by his own household.'],
  '06-03': ['夏后相覆亡，怀着身孕的后缗逃回有仍，少康在那里出生。后来他辗转避难，在有虞得到田地与部众，开始收拢夏人。', 'After Xiang’s fall, the pregnant Houmin escapes to Youreng, where Shaokang is born. After further flight, he gains land and followers in Youyu and begins gathering the Xia people.'],
  '06-04': ['夏桀召来商汤，将他囚于夏台，后来又放还。', 'Jie of Xia summons Tang, confines him at Xiatai and later releases him.'],
  '06-05': ['采桑的女子在空桑中发现婴儿伊尹。故事再向前追溯：洪水袭来，他的母亲离开故邑，回望时化作桑树。', 'A woman gathering mulberry leaves finds the infant Yi Yin in a hollow tree. The story looks back to his mother: escaping a flood, she turns toward her home and becomes a mulberry tree.'],
  '07-01': ['甲子吉日，穆天子拜会西王母。远行携来的白圭与玄璧，在相见时被郑重呈上。', 'On an auspicious jiazi day, King Mu visits the Queen Mother of the West. He presents the white gui and dark bi jade brought on his journey.'],
  '07-02': ['瑶池之上，穆天子与西王母以歌相答。她问他是否还会再来，他答，待东土事毕，还会重访。', 'At Yaochi, King Mu and the Queen Mother of the West exchange songs. She asks whether he will return; he promises another visit after attending to affairs in the east.'],
  '07-03': ['穆天子登上昆仑之丘，观看黄帝之宫与丰隆之葬，将所见留传后世。', 'King Mu ascends Kunlun Hill to see the Yellow Emperor’s palace and Fenglong’s burial place, passing the account on to later generations.'],
  '07-04': ['穆天子登上弇山，在山石上记下行迹，又种下一棵槐树。', 'King Mu climbs Mount Yan, records his journey on the stone and plants a huai tree.'],
};

export function referenceNarrative(record, locale) {
  const text = narratives[record.id] || narratives[record.properties.entity_id];
  return text?.[locale === 'en' ? 1 : 0] || '';
}

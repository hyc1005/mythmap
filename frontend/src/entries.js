export const entryTypes = { story: '故事', beast: '异兽', place: '地点与神域', domain: '神域', plant: '草木', water: '水域', material: '物产', passage: '经文段落', animal: '动物记载', valley: '谷地', wind: '风的记述', deity: '山神', rite: '祭礼' };

export function worldEntries(world) {
  return [
    ...world.beasts.map(item => ({ ...item, kind: 'beast' })),
    ...world.places.map(item => ({ ...item, kind: 'place' })),
    ...world.domains.map(item => ({ ...item, kind: 'domain' })),
    ...(world.natural_features || []),
    ...(world.passages || []),
    ...(world.text_entities || []),
  ].map(item => ({ ...item, entryType: entryTypes[item.kind] }));
}

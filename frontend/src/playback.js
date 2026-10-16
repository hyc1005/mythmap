export const BASE_PLAYBACK_RATE = 1.3;

export function playbackState({ error, ready, complete, blocked, reduced }) {
  if (error) return 'error';
  if (!ready) return 'loading';
  if (complete) return 'completed';
  if (blocked) return 'paused';
  return reduced ? 'manual' : 'playing';
}

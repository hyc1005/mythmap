import { useLocale } from '../i18n';
import { createPortal } from 'react-dom';
import { useCallback, useEffect, useRef, useState } from 'react';
import { AbsoluteFill, Easing, Img, interpolate, useCurrentFrame } from 'remotion';
import { Player } from '@remotion/player';
import { assetUrl } from '../asset-url';
import { loadImage } from '../asset-cache';
import { useReducedMotion } from '../motion';
import ArtworkImage from '../components/ArtworkImage';
import { BASE_PLAYBACK_RATE, playbackState } from '../playback';

const sceneUrl = name => assetUrl(`/data/atlas/myth-icons/scenes/${name}`);
const POSTER = sceneUrl('pangu-opening.webp');
const DURATION = 390;

function PanguComposition({ onAssetError }) {
  const frame = useCurrentFrame();
  const ease = Easing.inOut(Easing.cubic);
  const separation = interpolate(frame, [36, 120], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const reveal = interpolate(frame, [22, 62], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic) });
  const growth = interpolate(frame, [80, 320], [.78, 1.04], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const settle = interpolate(frame, [330, 389], [1, 0], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const groundY = interpolate(frame, [36, 125], [0, 18], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const skyY = interpolate(frame, [36, 125], [0, -13], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const light = interpolate(frame, [0, 32, 110, 250], [.08, .16, .58, .62], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const haze = interpolate(frame, [0, 70, 190], [.92, .44, .17], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });

  return <AbsoluteFill className="pangu-composition" data-frame={frame} style={{ backgroundColor: '#9e8355' }}>
    <div className="pangu-opening-light" style={{ opacity: light }} />
    <div className="pangu-chaos-haze" style={{ opacity: haze }} />
    <Img src={sceneUrl('pangu-cloud-layer.webp')} onError={onAssetError} className="pangu-layer pangu-sky-layer" style={{ transform: `translateY(${skyY}%) scale(${1 + separation * .05})` }} />
    <Img src={sceneUrl('pangu-earth-layer.webp')} onError={onAssetError} className="pangu-layer pangu-earth-layer" style={{ transform: `translateY(${groundY}%)` }} />
    <Img src={sceneUrl('pangu-supporting-figure.webp')} onError={onAssetError} className="pangu-layer pangu-person-layer" style={{ opacity: reveal, transform: `translateY(${(1 - reveal) * 9 - separation * 1.5}%) scale(${growth})` }} />
    <div className="pangu-settle" style={{ opacity: settle * .1 }} />
  </AbsoluteFill>;
}

export default function PanguOpening({ active, autoStart = true, selected, onStatusChange, onSkip, controlContainer, externalPaused = false, tourPlaying = null, onUserPlaybackChange }) {
  const { t } = useLocale();
  const wrapper = useRef(null);
  const player = useRef(null);
  const hasStarted = useRef(false);
  const ended = useRef(false);
  const manualPaused = useRef(false);
  const framePosition = useRef(0);
  const frameTimestamp = useRef(null);
  const animationFrame = useRef(null);
  const [visible, setVisible] = useState(false);
  const [pageVisible, setPageVisible] = useState(() => !document.hidden);
  const [playing, setPlaying] = useState(false);
  const [progressFrame, setProgressFrame] = useState(0);
  const [playbackRate, setPlaybackRate] = useState(1);
  const playbackRateRef = useRef(1);
  const [assetsReady, setAssetsReady] = useState(false);
  const [playerMounted, setPlayerMounted] = useState(false);
  const [failed, setFailed] = useState(false);
  const [retryKey, setRetryKey] = useState(0);
  const reducedMotion = useReducedMotion();
  const [manualScene, setManualScene] = useState(0);
  const status = playbackState({ error: failed, ready: reducedMotion || assetsReady, complete: ended.current,
    blocked: externalPaused || selected || !visible || !pageVisible || manualPaused.current,
    reduced: reducedMotion });
  useEffect(() => { onStatusChange(status); }, [status, onStatusChange]);

  const stopForError = useCallback(() => {
    setFailed(true);
    if (animationFrame.current !== null) cancelAnimationFrame(animationFrame.current);
    animationFrame.current = null;
    frameTimestamp.current = null;
    setPlaying(false);
  }, []);

  useEffect(() => {
    const node = wrapper.current;
    if (!node) return undefined;
    const observer = new IntersectionObserver(([entry]) => setVisible(entry.isIntersecting && entry.intersectionRatio >= .15), { threshold: [.15] });
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const update = () => setPageVisible(!document.hidden);
    document.addEventListener('visibilitychange', update);
    return () => document.removeEventListener('visibilitychange', update);
  }, []);

  useEffect(() => {
    if (reducedMotion) return undefined;
    let cancelled = false;
    setAssetsReady(false);
    const paths = ['pangu-cloud-layer.webp', 'pangu-earth-layer.webp', 'pangu-supporting-figure.webp'];
    Promise.all(paths.map(path => loadImage(`/data/atlas/myth-icons/scenes/${path}`))).then(() => { if (!cancelled) setAssetsReady(true); }).catch(() => { if (!cancelled) stopForError(); });
    return () => { cancelled = true; };
  }, [retryKey, reducedMotion, stopForError]);

  useEffect(() => {
    if (active && !selected && visible && pageVisible && assetsReady && !reducedMotion && !failed) setPlayerMounted(true);
  }, [active, selected, visible, pageVisible, assetsReady, reducedMotion, failed]);

  const stopClock = useCallback(() => {
    if (animationFrame.current !== null) cancelAnimationFrame(animationFrame.current);
    animationFrame.current = null;
    frameTimestamp.current = null;
    setPlaying(false);
  }, []);

  useEffect(() => {
    if (!active) {
      playbackRateRef.current = 1;
      setPlaybackRate(1);
    }
  }, [active]);

  const startClock = useCallback(() => {
    if (!player.current || animationFrame.current !== null || ended.current) return;
    hasStarted.current = true;
    setPlaying(true);
    const tick = timestamp => {
      if (frameTimestamp.current === null) frameTimestamp.current = timestamp;
      const elapsed = Math.max(0, timestamp - frameTimestamp.current);
      frameTimestamp.current = timestamp;
      framePosition.current = Math.min(DURATION, framePosition.current + elapsed * 30 / 1000 * BASE_PLAYBACK_RATE * playbackRateRef.current);
      const nextProgress = framePosition.current;
      setProgressFrame(current => Math.floor(current / 4) === Math.floor(nextProgress / 4) ? current : nextProgress);
      if (framePosition.current >= DURATION) {
        setProgressFrame(DURATION);
        player.current?.seekTo(DURATION - 1);
        animationFrame.current = null;
        frameTimestamp.current = null;
        ended.current = true;
        setPlaying(false);
        return;
      }
      player.current?.seekTo(Math.floor(framePosition.current));
      animationFrame.current = requestAnimationFrame(tick);
    };
    animationFrame.current = requestAnimationFrame(tick);
  }, []);

  useEffect(() => { if (tourPlaying === true) manualPaused.current = false; }, [tourPlaying]);
  useEffect(() => {
    if (!active || selected || externalPaused || !visible || !pageVisible || reducedMotion || failed || !assetsReady) {
      stopClock();
      return;
    }
    if (playerMounted && (autoStart || hasStarted.current) && !ended.current && !manualPaused.current) startClock();
  }, [active, autoStart, selected, externalPaused, tourPlaying, visible, pageVisible, reducedMotion, failed, assetsReady, playerMounted, retryKey, startClock, stopClock]);

  useEffect(() => () => { stopClock(); }, [stopClock]);

  const replay = () => {
    onUserPlaybackChange?.(true);
    ended.current = false;
    manualPaused.current = false;
    framePosition.current = 0;
    setProgressFrame(0);
    setManualScene(0);
    player.current?.seekTo(0);
    startClock();
  };
  const retry = () => {
    setFailed(false);
    ended.current = false;
    hasStarted.current = false;
    manualPaused.current = false;
    framePosition.current = 0;
    setRetryKey(value => value + 1);
  };

  const controls = <div className="pangu-player-controls" aria-label={t("盘古序章动画控制")}><progress value={progressFrame} max={DURATION} aria-label={t("盘古序章进度")} />
      {failed ? <button type="button" aria-label={t("重试盘古动态场景")} onClick={retry}>{t("重试动态场景")}</button> : reducedMotion ? <><span>{t("系统已减少动态效果")}</span><span>{t(['混沌初开', '天地分离', '盘古撑天', '天地成形'][manualScene])}</span><button onClick={() => { const next = Math.min(3, manualScene + 1); ended.current = next === 3; setManualScene(next); setProgressFrame(next * 130); }}>{t(manualScene >= 2 ? '完成故事' : '下一幕')}</button></> : !assetsReady ? <span>{t("场景载入中…")}</span> : !playerMounted ? <span>{autoStart ? t("进入画面后自动播放") : t("场景待播放")}</span> : <>
        <button type="button" aria-label={playing ? t("暂停盘古序章") : ended.current ? t("重播盘古序章") : hasStarted.current ? t("继续播放盘古序章") : t("播放盘古序章")} onClick={() => { if (playing) { manualPaused.current = true; stopClock(); onUserPlaybackChange?.(false); } else if (ended.current) replay(); else { manualPaused.current = false; startClock(); onUserPlaybackChange?.(true); } }}>{playing ? t("暂停") : ended.current ? t("播放完成 · 重播") : hasStarted.current ? t("继续播放") : t("播放")}</button>
        <details className="journey-more"><summary>{t('更多')}</summary><div>
        <button type="button" aria-label={t("重播盘古序章")} onClick={replay}>{t("重播")}</button>
        <button type="button" aria-label={t(`播放速度 ${playbackRate}倍`)} aria-pressed={playbackRate === 2} onClick={() => setPlaybackRate(rate => { const next = rate === 1 ? 2 : 1; playbackRateRef.current = next; return next; })}>{playbackRate}×</button>
        </div></details>
      </>}
      {!ended.current && <button onClick={onSkip}>{t('跳过')}</button>}
    </div>;

  return <div ref={wrapper} className="pangu-player-wrap" data-playback-rate={playbackRate} data-status={status}>
    {reducedMotion || failed || !assetsReady || !playerMounted ? <>
      <ArtworkImage className="pangu-static-poster" src={POSTER} alt={t("盤古分開混沌，天地初開木刻場景")} />
      {!reducedMotion && !failed && <span className="pangu-loading-note" role="status">{assetsReady ? autoStart ? t("进入画面后自动播放") : t("场景待播放") : t("场景载入中…")}</span>}
    </> : <Player
      key={retryKey}
      ref={player}
      component={PanguComposition}
      inputProps={{ onAssetError: stopForError }}
      durationInFrames={DURATION}
      fps={30}
      compositionWidth={1200}
      compositionHeight={800}
      loop={false}
      initiallyMuted
      controls={false}
      allowFullscreen={false}
      clickToPlay={false}
      moveToBeginningWhenEnded={false}
      acknowledgeRemotionLicense
      style={{ width: '100%', height: '100%' }}
    />}
    {controlContainer ? createPortal(controls, controlContainer) : controls}
  </div>;
}

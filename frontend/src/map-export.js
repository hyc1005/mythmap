export function drawMapLayers(context, canvases, styleFor = element => window.getComputedStyle(element)) {
  for (const canvas of canvases) {
    if (!canvas.width || !canvas.height) continue;
    const style = styleFor(canvas);
    const parentStyle = styleFor(canvas.parentElement);
    context.save();
    try {
      context.globalAlpha = Number(parentStyle.opacity || 1) * Number(style.opacity || 1);
      context.filter = style.filter || 'none';
      const transform = (style.transform || '').match(/^matrix\((.+)\)$/);
      context.setTransform(...(transform ? transform[1].split(',').map(Number) : [1, 0, 0, 1, 0, 0]));
      context.drawImage(canvas, 0, 0);
    } finally { context.restore(); }
  }
}

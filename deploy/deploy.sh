#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE="$ROOT/site"
MODE="${1:-serve}"
PORT="${PORT:-8080}"
TARGET=""
if [ "$MODE" = "serve" ]; then
  PORT="${2:-$PORT}"
else
  # Support both `copy /target` and the older `copy 8080 /target`.
  if [ -n "${3:-}" ] && [[ "${2:-}" =~ ^[0-9]+$ ]]; then
    PORT="$2"
    TARGET="$3"
  else
    TARGET="${2:-}"
  fi
fi

fail() { printf 'ERROR: %s\n' "$1" >&2; exit 1; }
confirm() {
  if [ "${FORCE:-0}" = "1" ]; then return; fi
  read -r -p "$1 [y/N] " answer
  case "$answer" in y|Y|yes|YES) ;; *) echo "Cancelled."; exit 0 ;; esac
}

echo "== MythMap static deployment =="
echo "Package: $ROOT"
echo "Mode:    $MODE"

[ "$MODE" = "serve" ] || [ "$MODE" = "copy" ] || fail "Mode must be serve or copy."

command -v python3 >/dev/null 2>&1 || fail "Python 3 is required to serve the package."
python3 -c 'import sys; raise SystemExit(0 if sys.version_info[0] == 3 else 1)' || fail "Python 3 is required."

for required in site/index.html site/opening-film.html site/data/myth-world.json site/assets; do
  [ -e "$ROOT/$required" ] || fail "Missing required path: $required"
done
[ -f "$ROOT/SHA256SUMS" ] || fail "SHA256SUMS is missing."

if command -v sha256sum >/dev/null 2>&1; then
  (cd "$ROOT" && sha256sum -c SHA256SUMS >/dev/null) || fail "Checksum verification failed."
elif command -v shasum >/dev/null 2>&1; then
  (cd "$ROOT" && shasum -a 256 -c SHA256SUMS >/dev/null) || fail "Checksum verification failed."
else
  fail "sha256sum or shasum is required."
fi
echo "Integrity: checksums match"

if [ "$MODE" = "serve" ]; then
  case "$PORT" in ''|*[!0-9]*) fail "Port must be a number." ;; esac
  [ "$PORT" -ge 1 ] && [ "$PORT" -le 65535 ] || fail "Port must be between 1 and 65535."
  if (exec 3<>"/dev/tcp/127.0.0.1/$PORT") 2>/dev/null; then
    exec 3>&- 2>/dev/null || true
    fail "Port $PORT is already in use."
  fi
  confirm "Deploy the verified static site now?"
  echo "Serving http://127.0.0.1:$PORT/  (Ctrl+C to stop)"
  exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$SITE"
else
  [ -n "$TARGET" ] || fail "Copy mode needs a target directory: ./deploy.sh copy 8080 /var/www/mythmap"
  TARGET="$(cd "$TARGET" 2>/dev/null && pwd || (mkdir -p "$TARGET" && cd "$TARGET" && pwd))"
  [ -w "$TARGET" ] || fail "Target is not writable: $TARGET"
  if [ -n "$(ls -A "$TARGET" 2>/dev/null)" ] && [ "${FORCE:-0}" != "1" ]; then
    fail "Target directory is not empty. Re-run with FORCE=1 to overwrite."
  fi
  confirm "Copy the verified static site to $TARGET now?"
  cp -R "$SITE"/. "$TARGET"/
  [ -f "$TARGET/index.html" ] || fail "Copy finished but index.html is missing."
  echo "Copied to $TARGET"
  echo "Point any static web server at this directory; no Node or API process is needed."
fi

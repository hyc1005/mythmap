#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
exec ./deploy.sh serve "${1:-8080}"

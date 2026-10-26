#!/usr/bin/env bash
# Weekly bank sweep: ingest any ~/harvests/* dirs missing from the ledger,
# verify, commit and push if anything changed. Safe to run any time.
set -uo pipefail
cd "$(dirname "$0")/.."

changed=0
for d in /home/ae/harvests/*/; do
  [ -d "$d" ] || continue
  if [ -d "$d/distilled" ] || [ -d "$d/condensed" ]; then
    out=$(python3 bank.py ingest "$d" 2>&1) || { echo "sweep: ingest failed for $d: $out"; continue; }
    case "$out" in
      INGESTED*) changed=1; echo "sweep: $out" ;;
    esac
  fi
done

dirty=$(git status --porcelain bank wiki/HOT.md 2>/dev/null)
if [ "$changed" = 1 ] || [ -n "$dirty" ]; then
  if ! python3 bank.py verify; then
    echo "sweep: verify FAILED — not committing; needs an agent pass"
    exit 1
  fi
  git add bank wiki/HOT.md
  git commit -m "bank: sweep $(date +%F) — ingest/synthesis" || exit 0
  git push || echo "sweep: push failed (retries next sweep)"
else
  echo "sweep: nothing new"
fi

#!/usr/bin/env python3
"""intel-distillations knowledge bank — ingest, verify, stats.

The bank is the ongoing layer on top of the static wiki: every tab harvest
gets ingested into an append-only ledger, distilled into a dated draft under
bank/harvests/, synthesized into wiki/ concepts, and turned into sourced
money moves under bank/moves/. Contract: bank/SCHEMA.md.

Design law: bank.py only touches DATA (ledger, structure, mechanical checks).
Prose synthesis is agent work; bank.py's verify step is the anti-fabrication
gate: every [fNN m:ss] citation must resolve to a mapped file whose text
actually contains that timestamp.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(ROOT, "bank")
LEDGER = os.path.join(BANK, "ledger.jsonl")
HARVESTS = os.path.join(BANK, "harvests")
MOVES = os.path.join(BANK, "moves")
MOVELOG = os.path.join(MOVES, "move-log.jsonl")

CIT_RE = re.compile(r"\[(f\d{2,}) (\d{1,2}:\d{2}(?::\d{2})?)\]")
MAP_RE = re.compile(r"^\|\s*(f\d{2,})\s*\|\s*([^|]+?)\s*\|\s*$", re.M)


def ts_seconds(ts):
    parts = [int(x) for x in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def corpus_dir(harvest_dir):
    for sub in ("distilled", "condensed"):
        d = os.path.join(harvest_dir, sub)
        if os.path.isdir(d):
            return d
    sys.exit(f"no distilled/ or condensed/ under {harvest_dir}")


def read_ledger():
    rows = []
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"FAIL ledger line {i}: {e}")
                    sys.exit(1)
    return rows


def append_ledger(row):
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def cmd_ingest(args):
    hdir = os.path.abspath(args.dir)
    if not os.path.isdir(hdir):
        sys.exit(f"no such harvest dir: {hdir}")
    m = re.search(r"(\d{4}-\d{2}-\d{2})", hdir)
    date = args.date or (m.group(1) if m else dt.date.today().isoformat())

    cdir = corpus_dir(hdir)
    os.makedirs(HARVESTS, exist_ok=True)
    draft = os.path.join(HARVESTS, f"{date}.md")
    if not os.path.exists(draft):
        with open(draft, "w", encoding="utf-8") as f:
            f.write(f"# Harvest {date} — draft pending\n\n"
                    f"Ingested from `{hdir}`.\n\n"
                    f"STATUS: mechanical ingest only. Synthesis pending — follow\n"
                    f"bank/SCHEMA.md section 3 (draft contract), then re-run\n"
                    f"`bank.py verify`.\n")

    ledger = read_ledger()
    if any(r.get("id") == date for r in ledger) and not args.force:
        print(f"SKIP {date}: already in ledger (use --force to re-ingest)")
        return
    files = sorted(os.listdir(cdir))
    lines = 0
    for f in files:
        with open(os.path.join(cdir, f), encoding="utf-8", errors="replace") as fh:
            lines += sum(1 for _ in fh)

    append_ledger({
        "id": date,
        "date": date,
        "kind": "harvest",
        "dir": hdir,
        "corpus": os.path.relpath(cdir, hdir),
        "files": len(files),
        "lines": lines,
        "ingested": dt.datetime.now().isoformat(timespec="seconds"),
    })

    draft = os.path.join(HARVESTS, f"{date}.md")
    if not os.path.exists(draft):
        with open(draft, "w", encoding="utf-8") as f:
            f.write(f"# Harvest {date} — draft pending\n\n"
                    f"Ingested {len(files)} files ({lines} lines) from `{hdir}`.\n\n"
                    f"STATUS: mechanical ingest only. Synthesis pending — follow\n"
                    f"bank/SCHEMA.md section 3 (draft contract), then re-run\n"
                    f"`bank.py verify`.\n")

    print(f"INGESTED {date}: {len(files)} files, {lines} lines -> ledger")
    print("next: write the synthesis draft (bank/SCHEMA.md s3), then:")
    print("  python3 bank.py verify && python3 bank.py stats")


def cmd_verify(args):
    ok = True
    ledger = read_ledger()
    dirs = {r["id"]: r["dir"] for r in ledger if r.get("kind") == "harvest"}

    for path in sorted(glob.glob(os.path.join(HARVESTS, "*.md"))):
        date = os.path.basename(path)[:-3]
        text = open(path, encoding="utf-8").read()
        if "draft pending" in text[:200]:
            print(f"WARN {date}: synthesis pending (draft stub)")
            continue
        if "already synthesized" in text[:200]:
            print(f"PASS {date}: imported at wiki build time (pointer only)")
            continue
        if date not in dirs:
            print(f"FAIL {date}: no ledger entry for this draft")
            ok = False
            continue
        cdir = corpus_dir(dirs[date])
        mapping = dict(MAP_RE.findall(text))
        if not mapping:
            print(f"FAIL {date}: no citation map table")
            ok = False
            continue
        for fid, fname in mapping.items():
            if not os.path.exists(os.path.join(cdir, fname)):
                print(f"FAIL {date}: map {fid} -> missing file {fname}")
                ok = False
        corpus_text = {}
        for fid, fname in mapping.items():
            fp = os.path.join(cdir, fname)
            if os.path.exists(fp):
                corpus_text[fid] = open(fp, encoding="utf-8", errors="replace").read()
        bad = 0
        for m in CIT_RE.finditer(text):
            fid, ts = m.group(1), m.group(2)
            if fid not in mapping:
                print(f"FAIL {date}: citation [{fid} {ts}] not in map")
                ok = False
                bad += 1
                continue
            want = ts_seconds(ts)
            hits = any(ts_seconds(x) == want
                       for x in re.findall(r"\d{1,2}:\d{2}(?::\d{2})?", corpus_text[fid]))
            if not hits:
                print(f"FAIL {date}: timestamp {ts} not found in {mapping[fid]}")
                ok = False
                bad += 1
        n_cit = len(CIT_RE.findall(text))
        print(f"{'PASS' if bad == 0 else 'FAIL'} {date}: {n_cit} citations checked, "
              f"{len(mapping)} mapped files")

    if os.path.exists(MOVELOG):
        with open(MOVELOG, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                    for key in ("id", "created", "move", "horizon", "sources", "status"):
                        if key not in row:
                            print(f"FAIL move-log line {i}: missing {key}")
                            ok = False
                except json.JSONDecodeError as e:
                    print(f"FAIL move-log line {i}: {e}")
                    ok = False
        print(f"PASS move-log checked" if ok else "move-log has failures")

    print("VERIFY: " + ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


def cmd_stats(args):
    ledger = read_ledger()
    rows = [r for r in ledger if r.get("kind") == "harvest"]
    print(f"harvests ingested: {len(rows)}")
    for r in rows:
        print(f"  {r['id']}: {r.get('files')} files, {r.get('lines')} lines")
    moves = []
    if os.path.exists(MOVELOG):
        with open(MOVELOG, encoding="utf-8") as f:
            moves = [json.loads(x) for x in f if x.strip()]
    by_status = {}
    for mv in moves:
        by_status[mv["status"]] = by_status.get(mv["status"], 0) + 1
    print(f"moves: {len(moves)} " + "(" + ", ".join(f"{k}:{v}" for k, v in sorted(by_status.items())) + ")" if moves else "moves: 0")
    drafts = sorted(os.path.basename(p) for p in glob.glob(os.path.join(HARVESTS, "*.md")))
    pending = [d for d in drafts if "draft pending" in open(os.path.join(HARVESTS, d), encoding="utf-8").read()[:200]]
    print(f"drafts: {len(drafts)} files, {len(pending)} pending synthesis")
    for d in pending:
        print(f"  PENDING {d}")


def main():
    ap = argparse.ArgumentParser(description="intel-distillations knowledge bank")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("ingest", help="ingest a harvest dir into the ledger")
    g.add_argument("dir")
    g.add_argument("--date")
    g.add_argument("--force", action="store_true")
    sub.add_parser("verify", help="verify ledger, drafts, citations, move log")
    sub.add_parser("stats", help="bank status summary")
    args = ap.parse_args()
    {"ingest": cmd_ingest, "verify": cmd_verify, "stats": cmd_stats}[args.cmd](args)


if __name__ == "__main__":
    main()

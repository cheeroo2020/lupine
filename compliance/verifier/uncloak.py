#!/usr/bin/env python3
import argparse, hashlib, json, os, sys

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Uncloak/verify a cloaked export against its anchor.json")
    ap.add_argument("export_file", help="Original export file to verify")
    ap.add_argument("anchor_json", help="Anchor JSON produced by anchor_cli.py")
    args = ap.parse_args()

    if not os.path.exists(args.export_file):
        raise SystemExit(f"Missing export file: {args.export_file}")
    if not os.path.exists(args.anchor_json):
        raise SystemExit(f"Missing anchor file: {args.anchor_json}")

    with open(args.anchor_json) as f:
        anchor = json.load(f)

    digest = sha256_file(args.export_file)

    ok = (anchor.get("digest") == digest)
    result = {
        "ok": ok,
        "expected": anchor.get("digest"),
        "observed": digest,
        "network": anchor.get("network"),
        "txid": anchor.get("txid"),
        "file": anchor.get("file"),
    }
    print(json.dumps(result, indent=2))
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse, hashlib, json, os, time, uuid

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Cloaked Compliance — anchor a file (mock testnet)")
    ap.add_argument("input", help="Path to export file (e.g., JSON/PDF)")
    ap.add_argument("--out", default="anchor.json", help="Output anchor record")
    args = ap.parse_args()

    if not os.path.exists(args.input):
        raise SystemExit(f"File not found: {args.input}")

    digest = sha256_file(args.input)
    record = {
        "id": str(uuid.uuid4()),
        "algo": "sha256",
        "digest": digest,
        "network": "polygon:testnet:mock",
        "txid": str(uuid.uuid4())[:16],
        "timestamp": int(time.time()),
        "file": os.path.basename(args.input),
    }
    with open(args.out, "w") as f:
        json.dump(record, f, indent=2)
    print(f"Anchored {args.input}")
    print(json.dumps(record, indent=2))

if __name__ == "__main__":
    main()

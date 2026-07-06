import hashlib
import os
import sys

def banner():
    print()
    print("MicroHash")
    print("=" * 40)

def digest(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def main():
    args = sys.argv[1:]

    if not args:
        banner()
        print("Usage:")
        print("  python3 -m microhash <file>")
        return

    filename = args[0]

    if not os.path.isfile(filename):
        print("File not found:", filename)
        return

    banner()
    print("File:", filename)
    print()

    for alg in ["md5", "sha1", "sha256", "sha512"]:
        print(f"{alg.upper():<8}: {digest(filename, alg)}")

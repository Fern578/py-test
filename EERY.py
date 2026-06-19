import os
import random
import string
import time
import zipfile
from pathlib import Path

# =========================
# SETTINGS
# =========================

MAKE_ZIP = True

# SAFE PATH (works everywhere: Windows, Linux, Pyodide)
BASE = Path.cwd() / "EERY_BUILD"
EERY_FOLDER = BASE / "EERY"
ZIP_PATH = BASE / "EERY_BUILD.zip"

# =========================
# HELPERS
# =========================

def rand_text(n):
    chars = string.ascii_letters + string.digits + "01!@#$%^&*()-_=+[]{}"
    return "".join(random.choice(chars) for _ in range(n))

def wait():
    time.sleep(0.5)

# =========================
# FAKE INSTALLER
# =========================

def installer():
    print("=" * 60)
    print("EERY INSTALLER".center(60))
    print("=" * 60)

    steps = [
        "Checking system environment...",
        "Allocating resources...",
        "Preparing directories...",
        "Downloading packages...",
        "Extracting data...",
        "Installing modules...",
        "Generating logs...",
        "Building file system...",
        "Finalizing installation...",
        "Cleaning up..."
    ]

    for i, step in enumerate(steps, 1):
        print(f"[{i}/10] {step}")
        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        wait()

    print("\nInstallation complete.\n")

# =========================
# FILE CREATION
# =========================

def create_files():
    EERY_FOLDER.mkdir(parents=True, exist_ok=True)

    # Core files
    base_files = {
        "ENCRYPTED.txt": "EE N CRYPTED BY ZOX U LOSER",
        "installed.txt": "EERY INSTALL COMPLETE",
        "Config.txt": "SYSTEM=TRUE\nSECURE=FALSE",
        "Users.txt": "ADMIN\nGUEST\nUNKNOWN",
        "Security.txt": "LEVEL: LOW",
        "Status.txt": "OK"
    }

    for name, content in base_files.items():
        (EERY_FOLDER / name).write_text(content)

    # Logs
    with open(EERY_FOLDER / "Logs.txt", "w") as f:
        for _ in range(1200):
            mode = random.randint(1, 3)
            if mode == 1:
                f.write("".join(random.choice("01") for _ in range(100)) + "\n")
            elif mode == 2:
                f.write(rand_text(80) + "\n")
            else:
                f.write(f"SYS-{random.randint(1000,9999)} MEM-{random.randint(10000,99999)}\n")

    # Random files
    for i in range(1, 25):
        with open(EERY_FOLDER / f"RANDOM_{i}.txt", "w") as f:
            for _ in range(120):
                f.write(rand_text(random.randint(40, 100)) + "\n")

    # System-style files
    system_files = [
        "KernelDump.txt",
        "MemoryTrace.txt",
        "Network.log",
        "Runtime.txt",
        "ProcessTable.txt",
        "DriverData.txt",
        "BootSequence.txt",
        "SystemState.txt"
    ]

    for name in system_files:
        with open(EERY_FOLDER / name, "w") as f:
            for _ in range(150):
                f.write(rand_text(70) + "\n")

# =========================
# ZIP EXPORT (OPTIONAL)
# =========================

def make_zip():
    if not MAKE_ZIP:
        print("ZIP disabled.")
        return

    print("Creating ZIP...")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in EERY_FOLDER.rglob("*"):
            zipf.write(file, file.relative_to(EERY_FOLDER))

    print("ZIP saved at:")
    print(ZIP_PATH)

# =========================
# MAIN
# =========================

def main():
    installer()
    create_files()

    print("EERY CREATED AT:")
    print(EERY_FOLDER)

    make_zip()

    print("\nDONE")

# Safe exit (no input() crash in Pyodide)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
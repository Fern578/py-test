import os
import random
import string
import time
import zipfile

# =========================
# SETTINGS
# =========================

USERNAME = "yesno"
MAKE_ZIP = True   # <-- toggle this ON/OFF

DESKTOP = fr"C:\Users\{USERNAME}\OneDrive\Desktop"
EERY_FOLDER = os.path.join(DESKTOP, "EERY")
ZIP_PATH = os.path.join(DESKTOP, "EERY_BUILD.zip")

# =========================
# HELPERS
# =========================

def rand_text(n):
    chars = string.ascii_letters + string.digits + "01!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(n))

# =========================
# FAKE INSTALLER
# =========================

def installer():
    print("=" * 60)
    print("EERY INSTALLER".center(60))
    print("=" * 60)

    steps = [
        "Initializing core modules...",
        "Loading system packages...",
        "Allocating memory...",
        "Creating directories...",
        "Generating data streams...",
        "Writing files...",
        "Compiling assets...",
        "Building logs...",
        "Finalizing installation...",
        "Cleaning temporary cache..."
    ]

    for i, step in enumerate(steps, 1):
        print(f"[{i}/10] {step}")
        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
        time.sleep(1)

    print("\nInstallation finished.\n")

# =========================
# FILE CREATION
# =========================

def create_eery():
    os.makedirs(EERY_FOLDER, exist_ok=True)

    # Base files
    base = {
        "ENCRYPTED.txt": "EE N CRYPTED BY ZOX U LOSER",
        "installed.txt": "EERY INSTALL COMPLETE",
        "Config.txt": "SYSTEM=TRUE\nSECURE=FALSE",
        "Users.txt": "ADMIN\nUNKNOWN\nGUEST",
        "Security.txt": "LEVEL: LOW",
    }

    for name, content in base.items():
        with open(os.path.join(EERY_FOLDER, name), "w") as f:
            f.write(content)

    # Logs
    with open(os.path.join(EERY_FOLDER, "Logs.txt"), "w") as f:
        for _ in range(1500):
            mode = random.randint(1, 3)
            if mode == 1:
                f.write("".join(random.choice("01") for _ in range(120)) + "\n")
            elif mode == 2:
                f.write(rand_text(90) + "\n")
            else:
                f.write(f"SYS-{random.randint(1000,9999)} MEM-{random.randint(10000,99999)}\n")

    # Many random files
    for i in range(1, 35):
        with open(os.path.join(EERY_FOLDER, f"RANDOM_{i}.txt"), "w") as f:
            for _ in range(150):
                f.write(rand_text(random.randint(50, 120)) + "\n")

    # System-like dumps
    sys_files = [
        "KernelDump.txt",
        "MemoryTrace.txt",
        "Network.log",
        "Runtime.txt",
        "ProcessTable.txt",
        "DriverData.txt",
        "BootSequence.txt",
        "SystemState.txt"
    ]

    for name in sys_files:
        with open(os.path.join(EERY_FOLDER, name), "w") as f:
            for _ in range(200):
                f.write(rand_text(80) + "\n")

# =========================
# ZIP (OPTIONAL)
# =========================

def make_zip():
    if not MAKE_ZIP:
        print("ZIP creation skipped (MAKE_ZIP = False)")
        return

    print("Creating ZIP file...")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(EERY_FOLDER):
            for file in files:
                full = os.path.join(root, file)
                arc = os.path.relpath(full, EERY_FOLDER)
                zipf.write(full, arc)

    print("ZIP created at:", ZIP_PATH)

# =========================
# MAIN
# =========================

def main():
    installer()

    print("Creating EERY folder...")
    create_eery()

    print("Files generated in:", EERY_FOLDER)

    make_zip()

    print("\nDONE")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
import os
import time
import random
import string
import tkinter as tk
from tkinter import messagebox

# =========================
# CONFIG
# =========================

TITLE = "EERY INSTALLER"
PASSWORD = "EERYDEV"
WAIT_TIME = 5

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

INSTALL_STEPS = [
    "Initializing installer core...",
    "Loading secure modules...",
    "Preparing environment...",
    "Downloading packages...",
    "Extracting resources...",
    "Installing runtime...",
    "Configuring system...",
    "Generating logs...",
    "Building file structure...",
    "Finalizing setup..."
]

# =========================
# UTIL
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def bar(p):
    w = 50
    f = int(w * p / 100)
    print(GREEN + "[" + "█"*f + "░"*(w-f) + f"] {p}%" + RESET)

def rand_text(n):
    chars = string.ascii_letters + string.digits + "01!@#$%^&*()-_=+"
    return "".join(random.choice(chars) for _ in range(n))

# =========================
# FILE GENERATION
# =========================

def create_eery():
    os.makedirs("EERY", exist_ok=True)

    # Core fixed files
    base_files = {
        "ENCRYPTED.txt": "EE N CRYPTED BY ZOX U LOSER",
        "installed.txt": "EERY INSTALL COMPLETE",
        "Config.txt": "SYSTEM=true\nSECURE=false\nDEBUG=0",
        "Users.txt": "ADMIN\nUNKNOWN\nGUEST",
        "Security.txt": "LEVEL: LOW",
        "Status.txt": "RUNNING OK",
    }

    for name, content in base_files.items():
        with open(f"EERY/{name}", "w") as f:
            f.write(content)

    # Logs (binary + mixed)
    with open("EERY/Logs.txt", "w") as f:
        for _ in range(1500):
            mode = random.randint(1, 3)
            if mode == 1:
                f.write("".join(random.choice("01") for _ in range(128)) + "\n")
            elif mode == 2:
                f.write(rand_text(90) + "\n")
            else:
                f.write(f"SYS-{random.randint(1000,9999)} MEM-{random.randint(10000,99999)}\n")

    # Random files
    for i in range(1, 31):
        with open(f"EERY/RANDOM_{i}.txt", "w") as f:
            for _ in range(200):
                f.write(rand_text(random.randint(40, 120)) + "\n")

    # System-like files
    sys_files = [
        "KernelDump.txt",
        "MemoryIndex.txt",
        "CacheTable.txt",
        "NetworkTrace.txt",
        "RuntimeLog.txt",
        "ProcessTable.txt",
        "BootSequence.txt",
        "DriverData.txt"
    ]

    for name in sys_files:
        with open(f"EERY/{name}", "w") as f:
            for _ in range(250):
                f.write(rand_text(80) + "\n")

# =========================
# GUI (SAFE)
# =========================

def open_gui():
    try:
        root = tk.Tk()
        root.title("EERY ACCESS PANEL")
        root.geometry("420x240")
        root.resizable(False, False)

        tk.Label(
            root,
            text="EERY ACCESS PANEL",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(root, text="Enter Password:").pack()

        entry = tk.Entry(root, show="*", width=30)
        entry.pack(pady=10)

        status = tk.Label(root, text="")
        status.pack()

        def check():
            if entry.get() == PASSWORD:
                status.config(text="ACCESS GRANTED")
                messagebox.showinfo("EERY", "Access Granted")
            else:
                status.config(text="ACCESS DENIED")

        tk.Button(root, text="Login", command=check).pack(pady=10)

        root.mainloop()

    except Exception as e:
        print("GUI ERROR:", e)

# =========================
# INSTALLER
# =========================

def installer():
    clear()

    print(GREEN + "="*60)
    print(TITLE.center(60))
    print("="*60 + RESET)

    print(CYAN + "\nStarting installation...\n" + RESET)

    for i, step in enumerate(INSTALL_STEPS, 1):
        print(YELLOW + "/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/" + RESET)
        print(CYAN + f"[{i}/10] {step}" + RESET)
        bar(i * 10)
        time.sleep(WAIT_TIME)

    create_eery()

    print(GREEN + "\nINSTALL COMPLETE\n" + RESET)
    print(CYAN + "EERY folder created with multiple files.\n" + RESET)

# =========================
# RUN SAFE
# =========================

if __name__ == "__main__":
    try:
        installer()
        open_gui()
    except Exception as e:
        print("FATAL ERROR:", e)

    input("\nPress Enter to exit...")
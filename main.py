import os
import subprocess
import time
import sys
import shutil

# --- CONFIG ---
CURRENT_DIR = "/home/john/Documents/GitHub/atmos-bridge"
HOME = os.path.expanduser("~")
ATMOS_ENGINE = os.path.join(CURRENT_DIR, "engine.py")
WINE_CMD = shutil.which("wine") or "/usr/bin/wine"

def get_file_manually(title):
    """Opens a file browser to select the .exe if the path is wrong."""
    try:
        path = subprocess.check_output([
            "zenity", "--file-selection",
            f"--title={title}",
            f"--filename={HOME}/.wine/drive_c/Program Files/"
        ]).decode().strip()
        return path
    except:
        return None

def launch_hub():
    # 1. Environment
    env = os.environ.copy()
    env["PYTHONPATH"] = CURRENT_DIR
    env["WINEASIO_NUMBER_OUTPUTS"] = "8"

    # 2. Start Engine
    print("🚀 Starting Atmos Bridge...")
    bridge_proc = subprocess.Popen([sys.executable, ATMOS_ENGINE], env=env)
    time.sleep(1)

    # 3. Main Selection
    apps = ["1", "FL Studio", "2", "Ableton Live", "3", "Manual Select", "4", "Quit"]
    cmd = ["zenity", "--list", "--column=ID", "--column=Software", "--height=300"] + apps

    try:
        choice = subprocess.check_output(cmd).decode().strip()
    except:
        bridge_proc.terminate()
        return

    # 4. Launch Logic with Auto-Fallback
    target_path = ""
    if "1" in choice:
        target_path = os.path.join(HOME, ".wine/drive_c/Program Files/Image-Line/FL Studio 20/FL64.exe")
    elif "2" in choice:
        # The path that failed you earlier
        target_path = os.path.join(HOME, ".wine/drive_c/Program Files/Ableton/Live 11 Suite/Program/Ableton Live 11 Suite.exe")

    # If path is wrong or "Manual Select" chosen, browse for it
    if not os.path.exists(target_path) or "3" in choice:
        print("⚠️ Default path failed or Manual Select chosen. Please select the .exe file.")
        target_path = get_file_manually("Select the DAW .exe File")

    if target_path and os.path.exists(target_path):
        print(f"🎹 Launching: {target_path}")
        subprocess.run([WINE_CMD, target_path], env=env)
    else:
        print("❌ No valid file selected.")

    # 5. Cleanup
    bridge_proc.terminate()
    print("✅ Cleaned.")

if __name__ == "__main__":
    launch_hub()

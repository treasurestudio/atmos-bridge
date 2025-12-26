import os
import sys
import time
import json

# --- 1. DYNAMIC PATHING ---
# Ensures the engine knows exactly where it is in your GitHub folder
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, "config.json")

def load_bridge_settings():
    """Safety check for config to prevent startup crashes."""
    if not os.path.exists(CONFIG_PATH):
        # Create a basic setup if the file is missing
        return {"buffer": 256, "channels": 8, "mode": "atmos"}
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except:
        return {"buffer": 256, "channels": 8}

def run_engine():
    print("--- ATMOS ROUTING ENGINE V1.0 ---")
    print(f"Working Directory: {CURRENT_DIR}")

    # 2. LOAD CONFIG
    settings = load_bridge_settings()
    channels = settings.get("channels", 8)

    print(f"🚀 Initializing {channels}-channel virtual bridge...")

    # 3. MOCK ROUTING LOGIC (Replace with your specific PipeWire/Mido calls)
    # This is the 'Heartbeat' that keeps the bridge alive.
    try:
        # Check for necessary audio libs
        import mido
        print("✅ MIDI backend connected.")
    except ImportError:
        print("⚠️ Warning: mido not found. MIDI control disabled.")

    print("🌌 Bridge is LIVE. Monitoring PipeWire nodes...")

    # 4. THE MAIN LOOP
    # Must have time.sleep to prevent the "Killed" (OOM) error.
    try:
        while True:
            # Your actual routing processing goes here.
            # Example: check_ports()

            time.sleep(0.1)  # 100ms heartbeat prevents CPU spiking
    except KeyboardInterrupt:
        print("\nStopping Engine...")

if __name__ == "__main__":
    # Ensure we don't run as root (can mess up PipeWire permissions)
    if os.geteuid() == 0:
        print("❌ Do not run the engine as sudo/root.")
        sys.exit(1)

    run_engine()

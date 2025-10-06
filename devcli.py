import sys
import os
import importlib
import json

# -----------------------------
# Ensure project root is in sys.path
# -----------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -----------------------------
# Import logger from utils
# -----------------------------
try:
    from utils.logger import setup_logger, log_action
except ImportError:
    print("[Error] Failed to import logger. Ensure utils/logger.py exists.")
    sys.exit(1)

setup_logger()

# -----------------------------
# Load config.json
# -----------------------------
CONFIG_PATH = os.path.join(PROJECT_ROOT, "config.json")
if not os.path.exists(CONFIG_PATH):
    config = {"modules": ["cert_manager", "key_management", "crypto", "code_signing", "verification"]}
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)
else:
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

# -----------------------------
# Dynamically load modules
# -----------------------------
module_objects = {}
for mod_name in config.get("modules", []):
    try:
        module_path = f"modules.{mod_name}"
        mod = importlib.import_module(module_path)
        if hasattr(mod, "main"):
            module_objects[mod_name] = mod
            log_action("devcli", f"Module '{mod_name}' loaded successfully")
        else:
            print(f"[Warning] Module '{mod_name}' has no main() function")
            log_action("devcli", f"Module '{mod_name}' has no main() function")
    except Exception as e:
        print(f"[Warning] Failed to load module '{mod_name}': {e}")
        log_action("devcli", f"Failed to load module '{mod_name}': {e}")

# -----------------------------
# CLI Menu
# -----------------------------
def main_menu():
    while True:
        print("\n=== DevCLI Multitool ===")
        if not module_objects:
            print("No modules loaded. Check config.json and modules folder!")
            break

        for i, mod in enumerate(module_objects.keys(), start=1):
            print(f"{i}) {mod.replace('_', ' ').title()}")
        print(f"{len(module_objects)+1}) Exit")

        choice = input("Select an option: ").strip()
        try:
            choice = int(choice)
            if choice == len(module_objects)+1:
                print("Exiting DevCLI...")
                break
            elif 1 <= choice <= len(module_objects):
                mod_name = list(module_objects.keys())[choice-1]
                try:
                    module_objects[mod_name].main(args=None)
                    log_action("devcli", f"Executed module '{mod_name}'")
                except Exception as e:
                    print(f"[Error] Module '{mod_name}' failed: {e}")
                    log_action("devcli", f"Module '{mod_name}' execution failed: {e}")
            else:
                print("Invalid choice! Try again.")
        except ValueError:
            print("Invalid input! Enter a number.")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main_menu()

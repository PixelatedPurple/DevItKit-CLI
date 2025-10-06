import subprocess
import sys

def install_dependencies():
    deps = ["cryptography", "colorama", "pyyaml", "rich"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", *deps])

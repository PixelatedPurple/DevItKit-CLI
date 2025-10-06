from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import os
from utils.logger import log_action

KEY_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "keys")

def main(args=None):
    file_path = input("Enter file path: ").strip()
    action = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    key_file = input("Enter key file path: ").strip()

    with open(key_file, "rb") as f:
        key_data = f.read()

    if action == "e":
        public_key = serialization.load_pem_public_key(key_data)
        with open(file_path, "rb") as f:
            plaintext = f.read()
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        out_file = file_path + ".enc"
        with open(out_file, "wb") as f:
            f.write(ciphertext)
        print(f"[Crypto] File encrypted -> {out_file}")
        log_action("crypto", f"Encrypted {file_path}")

    elif action == "d":
        private_key = serialization.load_pem_private_key(key_data, password=None)
        with open(file_path, "rb") as f:
            ciphertext = f.read()
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        out_file = file_path + ".dec"
        with open(out_file, "wb") as f:
            f.write(plaintext)
        print(f"[Crypto] File decrypted -> {out_file}")
        log_action("crypto", f"Decrypted {file_path}")

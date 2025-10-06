from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os
from utils.logger import log_action

def main(args=None):
    file_path = input("Enter file path to sign: ").strip()
    key_file = input("Enter private key path: ").strip()

    with open(key_file, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(file_path, "rb") as f:
        data = f.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    sig_file = file_path + ".sig"
    with open(sig_file, "wb") as f:
        f.write(signature)

    print(f"[CodeSigning] File signed -> {sig_file}")
    log_action("code_signing", f"Signed {file_path}")

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os
from utils.logger import log_action

KEY_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "keys")
os.makedirs(KEY_DIR, exist_ok=True)

def main(args=None):
    bits = 2048
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=bits)
    public_key = private_key.public_key()

    priv_path = os.path.join(KEY_DIR, "private_key.pem")
    pub_path = os.path.join(KEY_DIR, "public_key.pem")

    with open(priv_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open(pub_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print(f"[KeyManagement] Keys saved:\n Private: {priv_path}\n Public: {pub_path}")
    log_action("key_management", f"Generated {bits}-bit RSA key pair")

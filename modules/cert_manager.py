from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import os
from utils.logger import log_action

CERT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "keys")
os.makedirs(CERT_DIR, exist_ok=True)

def main(args=None):
    cn = input("Enter Common Name for certificate: ").strip()
    days = int(input("Enter validity days (default 365): ") or 365)

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cn)])
    cert = x509.CertificateBuilder().subject_name(subject)\
        .issuer_name(issuer)\
        .public_key(key.public_key())\
        .serial_number(x509.random_serial_number())\
        .not_valid_before(datetime.utcnow())\
        .not_valid_after(datetime.utcnow() + timedelta(days=days))\
        .sign(key, hashes.SHA256())

    cert_path = os.path.join(CERT_DIR, f"{cn}_cert.pem")
    key_path = os.path.join(CERT_DIR, f"{cn}_key.pem")
    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    with open(key_path, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    print(f"[CertManager] Certificate saved:\n Certificate: {cert_path}\n Key: {key_path}")
    log_action("cert_manager", f"Generated certificate {cn}")

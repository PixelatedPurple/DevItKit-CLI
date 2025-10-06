from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
import os
from utils.logger import log_action

def main(args=None):
    print("1) Verify Signature")
    print("2) Verify Certificate Expiry")
    choice = input("Select option: ").strip()

    if choice == "1":
        file_path = input("Enter signed file path: ").strip()
        sig_path = input("Enter signature file path: ").strip()
        pub_key_path = input("Enter public key path: ").strip()

        with open(file_path, "rb") as f:
            data = f.read()
        with open(sig_path, "rb") as f:
            signature = f.read()
        with open(pub_key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        try:
            public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print("[Verification] Signature is valid.")
            log_action("verification", f"Verified signature of {file_path}")
        except Exception:
            print("[Verification] Signature is INVALID!")
            log_action("verification", f"Signature INVALID for {file_path}")

    elif choice == "2":
        cert_path = input("Enter certificate file path: ").strip()
        with open(cert_path, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())
        if cert.not_valid_before <= x509.datetime.datetime.utcnow() <= cert.not_valid_after:
            print("[Verification] Certificate is valid.")
        else:
            print("[Verification] Certificate has expired or is not yet valid.")
        log_action("verification", f"Checked certificate {cert_path}")

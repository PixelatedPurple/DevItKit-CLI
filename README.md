# DevItKitv2 - Development CLI Multitool

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Dependencies](#dependencies)
5. [Setup & Installation](#setup--installation)
6. [Usage](#usage)
7. [Modules Documentation](#modules-documentation)

   * [Certificate Management](#certificate-management)
   * [Key Management](#key-management)
   * [Encryption / Decryption](#encryption--decryption)
   * [Code Signing](#code-signing)
   * [Verification](#verification)
8. [Logging](#logging)
9. [Extending DevItKitv2](#extending-devitkitv2)
10. [Notes](#notes)

---

## Overview

DevItKitv2 is a Python-based CLI multitool designed for developers and security enthusiasts.
It provides a centralized command-line interface to manage cryptographic operations including:

* Certificate generation and management
* Public/Private key generation
* File encryption and decryption
* Code signing and verification
* Extensive logging
* Dynamic module loading for future expansion

---

## Features

* Interactive CLI menu for easy navigation
* Centralized configuration via `config.json`
* Dynamic module loading
* Logging with timestamp and date (`data/logs/cli.log`)
* Fully modular architecture: easily add new modules
* Supports RSA key management, X.509 certificate creation, encryption/decryption, and signing

---

## Project Structure

```
DevItKitv2/
│ devcli.py               # Main CLI entry point
│ config.json             # Configuration file for modules
│ requirements.txt        # Python dependencies
│ README.md               # Project documentation
│ utils/
│   ├ __init__.py
│   └ logger.py           # Logging utilities
│ modules/
│   ├ __init__.py
│   ├ cert_manager.py     # Certificate management module
│   ├ key_management.py   # Key generation module
│   ├ crypto.py           # File encryption/decryption module
│   ├ code_signing.py     # Code signing module
│   └ verification.py     # Signature & certificate verification
│ data/
│   ├ keys/               # Generated keys & certificates
│   └ logs/               # Log files
```

---

## Dependencies

DevItKitv2 requires the following Python packages:

* `cryptography>=41.0.0` - Core cryptography operations
* `colorama>=1.5.0` *(optional)* - CLI color output
* `PyYAML>=6.0` *(optional)* - Future config expansion

Install all dependencies using:

```bash
python -m pip install -r requirements.txt
```

> Make sure to use the same Python executable you will run `devcli.py` with.

---

## Setup & Installation

1. Clone or download the project to your local machine.
2. Ensure Python 3.10+ or 3.13 is installed.
3. Install dependencies using `pip install -r requirements.txt`.
4. Verify folder structure: `data/keys` and `data/logs` exist (DevCLI creates them automatically on first run).
5. Run DevCLI:

```bash
python devcli.py
```

---

## Usage

1. Launch `devcli.py`.
2. You will see an interactive CLI menu listing all available modules.
3. Select a module by number and follow prompts to execute tasks.
4. Exit by selecting the `Exit` option.

---

## Modules Documentation

### Certificate Management

* Generates X.509 certificates with a user-specified Common Name (CN).
* Saves certificate and private key in `data/keys/`.
* Uses `cryptography.x509` for certificate creation.

### Key Management

* Generates RSA public/private key pairs (2048-bit by default).
* Saves keys as PEM files in `data/keys/`.

### Encryption / Decryption

* Encrypts files using a public key.
* Decrypts files using a private key.
* Uses RSA + OAEP padding.

### Code Signing

* Signs a file with a private key.
* Generates a `.sig` signature file.
* Uses RSA + PSS padding with SHA-256.

### Verification

* Verifies a signature with a public key.
* Checks certificate validity dates.
* Provides feedback if signature or certificate is invalid.

---

## Logging

* All module actions are logged with timestamp in `data/logs/cli.log`.
* Example log entry:

```
2025-10-06 17:00:00 | INFO | [key_management] Generated 2048-bit RSA key pair
```

---

## Extending DevItKitv2

* Add a new module by creating a `.py` file in `modules/`.
* Implement a `main(args=None)` function in the module.
* Add the module name to `config.json` under `"modules"`.
* The CLI will automatically detect and load it.

---

## Notes

* Ensure `cryptography` is installed in the **same Python environment** used to run DevCLI.
* Use Python virtual environments to avoid module conflicts.
* DevItKitv2 is modular and can be extended to include additional cryptographic or developer utilities.

---

**DevItKitv2** – Secure, modular, and developer-friendly CLI multitool for cryptography and code management.

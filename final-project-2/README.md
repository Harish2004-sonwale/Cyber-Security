# Secure File Storage System

A secure file storage system that encrypts files using AES-256 encryption with integrity verification.

## Features

- AES-256 encryption using cryptography library
- Secure key generation using Scrypt
- File integrity verification using SHA-256
- Metadata storage for encrypted files
- Modern GUI interface using PyQt5
- Secure password handling
- Encrypted files with .enc extension
- Automatic hash verification
- Secure storage of encryption parameters

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### GUI Interface
Run the application:
```bash
python secure_storage.py
```

The GUI will open with the following options:
1. Enter a password (must be remembered for decryption)
2. Click "Encrypt File" to select and encrypt a file
3. Click "Decrypt File" to select and decrypt an .enc file

### File Operations
- Encrypted files are stored in the `encrypted_files` directory
- Each encrypted file has a .enc extension
- Metadata is stored in `encrypted_files/metadata.json`
- Files can only be decrypted with the correct password

## Security Features

- AES-256 encryption with CBC mode
- Secure key derivation using Scrypt
- File integrity verification using SHA-256
- Secure storage of encryption parameters
- Password-based encryption
- Automatic hash verification

## File Structure

```
encrypted_files/
├── metadata.json       # Stores file metadata and encryption parameters
└── *.enc              # Encrypted files
```

## Security Notes

1. Always use a strong password
2. Keep your password secure
3. Backup your metadata.json file
4. Store encrypted files securely
5. Keep your password manager secure

## License

This project is licensed under the MIT License - see the LICENSE file for details.

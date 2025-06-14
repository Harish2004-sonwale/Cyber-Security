import os
import sys
import json
import hashlib
import base64
from datetime import datetime
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QFileDialog, 
                           QTextEdit, QLineEdit, QMessageBox, QProgressBar)
from PyQt5.QtCore import Qt

class SecureStorage:
    def __init__(self, storage_dir='encrypted_files', key_size=32):
        self.storage_dir = Path(storage_dir)
        self.key_size = key_size
        self.storage_dir.mkdir(exist_ok=True)
        self.metadata_file = self.storage_dir / 'metadata.json'
        self.metadata = self._load_metadata()

    def _load_metadata(self):
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_metadata(self):
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)

    def _generate_key(self, password: str) -> bytes:
        """Generate AES-256 key using Scrypt"""
        salt = os.urandom(16)
        kdf = Scrypt(
            salt=salt,
            length=self.key_size,
            n=2**14,
            r=8,
            p=1,
        )
        key = kdf.derive(password.encode())
        return key, base64.b64encode(salt).decode()

    def _encrypt_file(self, file_path: Path, password: str) -> tuple:
        """Encrypt file using AES-256"""
        try:
            key, salt = self._generate_key(password)
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()

            with open(file_path, 'rb') as f:
                data = f.read()
                padded_data = padder.update(data) + padder.finalize()
                encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            # Calculate hash for integrity verification
            file_hash = hashlib.sha256(data).hexdigest()

            # Create encrypted file path
            encrypted_path = self.storage_dir / f"{file_path.stem}.enc"
            with open(encrypted_path, 'wb') as f:
                f.write(base64.b64encode(iv))
                f.write(encrypted_data)

            # Update metadata
            timestamp = datetime.now().isoformat()
            metadata = {
                'original_name': file_path.name,
                'encrypted_name': encrypted_path.name,
                'timestamp': timestamp,
                'file_hash': file_hash,
                'salt': salt
            }
            self.metadata[file_path.name] = metadata
            self._save_metadata()

            return True, metadata

        except Exception as e:
            return False, str(e)

    def _decrypt_file(self, encrypted_path: Path, password: str) -> tuple:
        """Decrypt file using AES-256"""
        try:
            metadata = self.metadata.get(encrypted_path.stem)
            if not metadata:
                return False, "File not found in metadata"

            # Verify file hash
            with open(encrypted_path, 'rb') as f:
                f.seek(0)
                iv = base64.b64decode(f.read(24))  # IV is 24 bytes in base64
                encrypted_data = f.read()

            # Generate key using stored salt
            kdf = Scrypt(
                salt=base64.b64decode(metadata['salt']),
                length=self.key_size,
                n=2**14,
                r=8,
                p=1,
            )
            key = kdf.derive(password.encode())

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            unpadder = padding.PKCS7(128).unpadder()

            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
            original_data = unpadder.update(decrypted_data) + unpadder.finalize()

            # Verify hash
            calculated_hash = hashlib.sha256(original_data).hexdigest()
            if calculated_hash != metadata['file_hash']:
                return False, "File integrity check failed"

            # Create decrypted file
            decrypted_path = Path(encrypted_path.stem)
            with open(decrypted_path, 'wb') as f:
                f.write(original_data)

            return True, decrypted_path

        except Exception as e:
            return False, str(e)

class SecureStorageGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.storage = SecureStorage()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Secure File Storage System")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Password input
        password_group = QWidget()
        password_layout = QHBoxLayout(password_group)
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        layout.addWidget(password_group)

        # File operations buttons
        buttons_group = QWidget()
        buttons_layout = QHBoxLayout(buttons_group)
        
        self.encrypt_button = QPushButton("Encrypt File")
        self.encrypt_button.clicked.connect(self.encrypt_file)
        
        self.decrypt_button = QPushButton("Decrypt File")
        self.decrypt_button.clicked.connect(self.decrypt_file)
        
        buttons_layout.addWidget(self.encrypt_button)
        buttons_layout.addWidget(self.decrypt_button)
        layout.addWidget(buttons_group)

        # Status text
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        layout.addWidget(self.status_text)

        # Progress bar
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

    def encrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File to Encrypt",
            "",
            "All Files (*.*)"
        )
        if file_path:
            password = self.password_input.text()
            if not password:
                QMessageBox.warning(self, "Error", "Please enter a password")
                return

            success, result = self.storage._encrypt_file(Path(file_path), password)
            if success:
                self.status_text.append(f"Successfully encrypted file: {file_path}\nMetadata: {json.dumps(result, indent=2)}")
            else:
                QMessageBox.warning(self, "Error", f"Encryption failed: {result}")

    def decrypt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File to Decrypt",
            "",
            "Encrypted Files (*.enc)"
        )
        if file_path:
            password = self.password_input.text()
            if not password:
                QMessageBox.warning(self, "Error", "Please enter a password")
                return

            success, result = self.storage._decrypt_file(Path(file_path), password)
            if success:
                self.status_text.append(f"Successfully decrypted file: {file_path}\nDecrypted to: {result}")
            else:
                QMessageBox.warning(self, "Error", f"Decryption failed: {result}")

def main():
    app = QApplication(sys.argv)
    window = SecureStorageGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

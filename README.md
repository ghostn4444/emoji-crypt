# 🔐 Emoji Crypt

Securely encrypt and hide messages inside emojis using strong cryptography.

Emoji Crypt combines modern encryption with a playful encoding layer, transforming sensitive messages into harmless-looking emoji sequences.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

* 🔐 Strong encryption using Fernet (AES + HMAC)
* 🔑 Password-based key derivation (PBKDF2 + SHA-256)
* 🧂 Random salt for enhanced security
* 😊 Emoji-based encoding layer
* 🔄 Full encode/decode support
* 🖥️ Simple CLI interface

---

## 📸 Example

**Input:**

```
test
```

**Encrypted Output:**

```
🙈🚗🛭🚘🛏🙋🚞🙟🛳...
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/emoji-crypt.git
cd emoji-crypt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the tool:

```bash
python main.py
```

Example interface:

```
==================================================
🔐 EMOJI CRYPTO TOOL 🔐
Strong encryption + hidden emoji messages
==================================================

1 - Encrypt
2 - Decrypt
0 - Exit
Choose: <OPTION>
```

---

## 🔐 How It Works

1. The user inputs a message and password
2. A random salt is generated
3. A secure key is derived using PBKDF2 (SHA-256)
4. The message is encrypted using Fernet
5. The encrypted bytes are converted into emojis

---

## ⚠️ Security Notes

* Use strong passwords (recommended: 12+ characters)
* Fernet provides authenticated encryption (AES + HMAC)
* Emoji encoding is **not encryption**, only an obfuscation layer

---

## 📦 Dependencies

```
cryptography
```

---

## 📜 License

MIT License

---

## 👨‍💻 Author

[@GhostN4444](https://github.com/GhostN4444)


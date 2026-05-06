import base64
import os
import hashlib
from cryptography.fernet import Fernet

BASE_EMOJI = 0x1F600


def banner():
    print("=" * 50)
    print("🔐 EMOJI CRYPTO TOOL 🔐")
    print("Criptografia forte + mensagens escondidas em emoji")
    print("=" * 50)


def derive_key(password, salt):
    kdf = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return base64.urlsafe_b64encode(kdf)


def text_to_emoji(text):
    return ''.join(chr(BASE_EMOJI + b) for b in text)


def emoji_to_text(emojis):
    return bytes([ord(e) - BASE_EMOJI for e in emojis])


def encrypt():
    text = input("Digite a mensagem: ")
    password = input("Digite a senha: ")

    salt = os.urandom(16)
    key = derive_key(password, salt)

    f = Fernet(key)
    token = f.encrypt(text.encode())

    payload = salt + token
    emoji_msg = text_to_emoji(payload)

    print("\n🔒 Mensagem criptografada:")
    print(emoji_msg)


def decrypt():
    emoji_msg = input("Cole a mensagem em emoji: ")
    password = input("Digite a senha: ")

    try:
        data = emoji_to_text(emoji_msg)

        salt = data[:16]
        token = data[16:]

        key = derive_key(password, salt)
        f = Fernet(key)

        decrypted = f.decrypt(token).decode()

        print("\n🔓 Mensagem original:")
        print(decrypted)

    except Exception:
        print("\n❌ Erro: senha incorreta ou mensagem inválida.")

def menu():
    while True:
        print("\n1 - Criptografar")
        print("2 - Descriptografar")
        print("0 - Sair")

        choice = input("Escolha: ")

        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    banner()
    menu()

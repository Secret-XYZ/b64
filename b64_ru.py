import base64


def code_tool():
    print("MENU (base64)\n")
    print("[1] Зашифровать")
    print("[2] Расшифровать")
    choice = input("\nВыберите элемент: ")

    if choice == "1":
        print("\nВставьте то, что хотите преобразовать в base64, затем нажмите Enter, а после этого — Ctrl + D:")
        import sys
        original_code = sys.stdin.read()

        if original_code.strip():
            encoded_bytes = base64.b64encode(original_code.encode('utf-8'))
            encoded_string = encoded_bytes.decode('utf-8')

            print("\n" + " " * 30)
            print("Result:")
            print(encoded_string)
            print(f"\nCode:\nimport base64\nexec(base64.b64decode('{encoded_string}').decode('utf-8'))")

    elif choice == "2":
        encoded_string = input("\nВставьте base64 для расшифровки: ").strip()
        try:
            decoded_bytes = base64.b64decode(encoded_string)
            decoded_code = decoded_bytes.decode('utf-8')

            print("\nResult:")
            print(decoded_code)
        except Exception as e:
            print(f"\nНе удалось расшифровать. Проверьте, правильно ли скопирована строка.")


if __name__ == "__main__":
    code_tool()

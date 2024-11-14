def caesar_cipher_encrypt():
    while True:
        shift = input("Введіть значення зсуву (1-25): ")
        if shift.isdigit() and 1 <= int(shift) <= 25:
            shift = int(shift)
            break
        else:
            print("Будь ласка, введіть дійсне значення зсуву.")

    text = input("Введіть текст для шифрування: ")
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    print("Encrypted text:", encrypted_text)

caesar_cipher_encrypt()

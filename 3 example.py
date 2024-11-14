text = input("Enter your message: ")
cipher = ''

for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 3

    if code > ord('Z'):
        code = code - 26

    cipher += chr(code)

print(cipher)


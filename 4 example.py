cipher = input('Enter your cryptogram: ')
text = ''

for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 3
    if code < ord('A'):
        code = code + 26
    text += chr(code)

print(text)

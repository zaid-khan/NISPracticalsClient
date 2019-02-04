def caesar_encryption(str, key_value):
    ct = ""
    for s in str:
        if s == ' ':
            continue
        ascii_value = ord(s) - 97
        ct += chr(((ascii_value + key_value) % 26 + 97))
    return ct
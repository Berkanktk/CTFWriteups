flag = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"


def encrypt_rot13(text):
    result = ""
    for char in text:
        ascii_val = ord(char)
        if ord('a') <= ascii_val <= ord('z'):
            ascii_val = (ascii_val - ord('a') + 13) % 26 + ord('a')
        elif ord('A') <= ascii_val <= ord('Z'):
            ascii_val = (ascii_val - ord('A') + 13) % 26 + ord('A')
        result += chr(ascii_val)
    return result


def decrypt_rot13(text):
    return encrypt_rot13(text)


if __name__ == '__main__':
    print(decrypt_rot13(flag))

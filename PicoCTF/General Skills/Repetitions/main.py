import base64

with open('enc_flag', 'r') as f:
    enc = f.read()


def nested_bas64_decode(enc):
    while True:
        enc = base64.b64decode(enc).decode()

        if 'pico' in enc:
            print(enc)
            break


nested_bas64_decode(enc)

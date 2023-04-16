alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
           "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
encoded_str = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

decoded_str = ""
for c in encoded_str:
    index = alphabet.index(c)
    decoded_index = (index - 47) % len(alphabet)
    decoded_char = alphabet[decoded_index]
    decoded_str += decoded_char

print(decoded_str)

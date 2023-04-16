message = 'gvswwmrkxlivyfmgsrhnrisegl'  # encrypted message
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(LETTERS) + 1):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Key #%s: picoCTF{%s}' % (key, translated))

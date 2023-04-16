flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"


def main():
    for i in range(len(flag)):
        print(chr(ord(flag[i]) >> 8), end="")
        print(chr((ord(flag[i])) - ((ord(flag[i]) >> 8) << 8)), end="")


main()

# decoded = ''.join([chr(ord(flag[i]) >> 8) + chr(ord(flag[i]) - (ord(flag[i]) >> 8 << 8)) for i in range(len(flag))])
# print(decoded)

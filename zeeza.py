"""Caesar_V1 by ศิษย์เทพปอง#2"""
def caesar():
    """Func. caesar for decode the password"""
    num = int(input())
    text = input()
    for i in text:
        if i.isalpha() and i.islower():
            dog = ord(i) + num
            if dog > 122:
                dog = ord(i) - 26 + num
                print(chr(dog), end='')
            elif 97 <= dog <= 122:
                print(chr(dog), end='')
            else:
                if num >= -26:
                    dog = ord(i) + 26 + num
                    print(chr(dog), end='')
                else:
                    dog = ord(i) + 26 + num + abs(num) + 26
                    print(chr(dog), end='')
        elif i.isalpha() and i.upper():
            dog = ord(i) + num
            if dog > 90:
                dog = ord(i) - 26 + num
                print(chr(dog), end='')
            elif 65 <= dog <= 90:
                print(chr(dog), end='')
            else:
                if num >= -26:
                    dog = ord(i) + 26 + num
                    print(chr(dog), end='')
                else:
                    dog = ord(i) + 26 + num + 26
                    print(chr(dog), end='')
        else:
            print(i, end="")
caesar()

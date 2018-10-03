"""Docstring"""
def main():
    """Function Main for finding the largest number"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    #dog, cat, egg, fat are the collector of the more number
    dog = 0
    dog += (ver(num1, num2))
    cat = 0
    cat += (ver(num3, num4))
    egg = 0
    egg += (ver(num5, num6))
    fat = 0
    fat += (ver(num7, num8))
    if dog > cat and dog > egg and dog > fat:
        print(dog)
    elif cat > dog and cat > egg and cat > fat:
        print(cat)
    elif egg > cat and egg > dog and egg > fat:
        print(egg)
    elif fat > cat and fat > dog and fat > egg:
        print(fat)
def ver(ant, boy):
    """Function Ver for compare the more number"""
    if ant > boy:
        return ant
    else:
        return boy
main()

"""Is P' Guy love you?"""
def main():
    """Main Func."""
    sex = input()
    high = float(input())
    weigh = float(input())
    veg = input()
    grade = float(input())
    if sex == "male":
        fan = int(input())
        if (high >= 180 and 60 < weigh < 80 and veg == "Y"\
             and grade >= 3 and fan <= 3)or grade == 4:
            print("\"P' Guy Love You!\"")
        else:
            print("\"Not you!\"")
    else:
        if (high <= 170 and weigh <= 60 and veg == "Y"\
             and grade >= 3) or grade == 4:
            print("\"P' Guy Love You!\"")
        else:
            print("\"Not you!\"")
main()

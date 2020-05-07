"""00XX: Yes, Sir ! Chef !"""
def main():
    """Main Func."""
    food_1 = int(input())
    food_2 = int(input())
    food_3 = int(input())
    food_4 = int(input())
    food_5 = int(input())
    food_6 = int(input())
    long_len = max(len(str(food_1)), len(str(food_2)), len(str(food_3)), len(str(food_4)), len(str(food_5)), len(str(food_6)))
    
    if food_1 == 0 and food_2 == 0 and food_3 == 0 and food_4 == 0 and food_5== 0:
        print()
    else:
        if food_1 != 0:
            print("Baked Potato%s%d" %("_"*(12 + long_len - len(str(food_1))), food_1))
        if food_2 != 0:
            print("Aglio Olio Spaghetti%s%d" %("_"*(4 + long_len - len(str(food_2))), food_2))
        if food_3 != 0:
            print("Tenderloin Steak%s%d" %("_"*(8 + long_len - len(str(food_3))), food_3))
        if food_4 != 0:
            print("Rib Eye Steak%s%d" %("_"*(11 + long_len - len(str(food_4))), food_4))
        if food_5 != 0:
            print("New York Steak%s%d" %("_"*(10 + long_len - len(str(food_5))), food_5))
        if food_6 != 0:
            print("Porterhouse%s%d" %("_"*(13 + long_len - len(str(food_6))), food_6))
main()
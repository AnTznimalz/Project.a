"""00XX: Yes, Sir ! Chef !"""
def main():
    """Main Func."""
    food_1 = int(input())
    food_2 = int(input())
    food_3 = int(input())
    food_4 = int(input())
    food_5 = int(input())
    food_6 = int(input())
    max_len = 20 if food_2 > 0 else 16 
    max_len = 16 if food_3 > 0 and food_2 == 0 else 14 
    max_len = 14 if food_5 > 0 and food_2 == 0 and food_3 == 0 else 13 
    max_len = 13 if food_4 > 0 and food_2 == 0 and food_3 == 0 and food_5 == 0 else 12 
    max_len = 12 if food_1 > 0 and food_2 == 0 and food_3 == 0 and food_5 == 0 and food_4 == 0 else 11  
    long_len = max(len(str(food_1)), len(str(food_2)), \
    len(str(food_3)), len(str(food_4)), len(str(food_5)), len(str(food_6)))
    reserve = long_len
    if food_1 == 0 and food_2 == 0 and food_3 == 0 and food_4 == 0 and food_5 == 0:
        print()
    else:
        if food_1 != 0:#12 12
            if max_len == 12:
                long_len = 0
            else:
                long_len -= len(str(food_1))
            print("Baked Potato%s%d" %("_"*(max_len - 12 + 4 + long_len), food_1))
            long_len = reserve
        if food_2 != 0:#20 4
            if max_len == 20:
                long_len = 0
            else:
                long_len -= len(str(food_2))
            print("Aglio Olio Spaghetti%s%d" %("_"*(max_len - 20 + 4 + long_len), food_2))
            long_len = reserve
        if food_3 != 0:#16 8
            if max_len == 16:
                long_len = 0
            else:
                long_len -= len(str(food_3))
            print("Tenderloin Steak%s%d" %("_"*(max_len - 16 + 4 + long_len), food_3))
            long_len = reserve
        if food_4 != 0:#13 11
            if max_len == 13:
                long_len = 0
            else:
                long_len -= len(str(food_4))
            print("Rib Eye Steak%s%d" %("_"*(max_len - 13 + 4 + long_len), food_4))
            long_len = reserve
        if food_5 != 0:#14 10
            if max_len == 14:
                long_len = 0
            else:
                long_len -= len(str(food_5))
            print("New York Steak%s%d" %("_"*(max_len - 14 + 4 + long_len), food_5))
            long_len = reserve
        if food_6 != 0:#11 13
            if max_len == 11:
                long_len = 0
            else:
                long_len -= len(str(food_6))
            print("Porterhouse%s%d" %("_"*(max_len - 11 + 4 + long_len), food_6))
            long_len = reserve
main()

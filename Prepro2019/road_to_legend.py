"""0068: Road to Legend"""
def main():
    """Main Func."""
    num = int(input())
    count = 0
    time = 0
    while count <= num:
        text = input()
        if text == "WIN":
            count += 1
        else:
            if count > 0:
                count -= 1
        time += 15
    hour = time//60
    minute = (time - hour*60)
    if minute != 0:
        minute = (100/(60/minute))/100
    print("Congratulations, You've played %.2f hour(s)." %(hour+minute))
main()

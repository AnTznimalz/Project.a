"""(loop)Set the alarm!!!"""
def main():
    """Main Func."""
    text = input()
    time = 0
    while text != "stop":
        text = input()
        time += 10
    hour = 6 + time // 60
    minute = time % 60
    if hour >= 24:
        hour -= 24
    print("%02d:%02d" %(hour, minute))
    if time >= 210:
        print("You are fired!")
main()
    
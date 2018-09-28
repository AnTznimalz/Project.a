"""PenPineAppleApplePen"""
def power():
    """Func. Power for check lyrics"""
    stat = "0"
    while True:
        text = input()
        if text == "Pen" and stat == "0":
            stat = "1"
        elif text == "Pineapple" and stat == "1":
            stat = "2"
        elif text == "Apple" and stat == "2":
            stat = "3"
        elif text == "Pen" and stat == "3":
            print("Correct lyrics!")
            break
        elif text == "Pen" and stat != "0":
            print("Wrong lyrics!")
            stat = "1"
        else:
            print("Wrong lyrics!")
            stat = "0"
power()

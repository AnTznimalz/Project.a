"""0012: Time Conversion"""
def main(time=int(input())):
    """Func. main"""
    hour, minute, sec = 0, 0, 0
    hour = time // 3600
    time -= hour*3600
    minute = time // 60
    time -= minute*60
    sec = time
    time = 0
    print("%d hour(s) %d minute(s) %d second(s)." %(hour, minute, sec))
main()

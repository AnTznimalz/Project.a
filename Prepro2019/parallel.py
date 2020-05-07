"""1016: Parallel World"""
def main():
    """Main Func."""
    test = int(input())
    sec = int(input())
    minute = int(input())
    hour = int(input())
    hrs = test // (sec * minute)
    test -= hrs * sec * minute
    mins = test // sec
    test -= mins * sec
    if hour < hrs:
        hrs -= hour * (hrs // hour)
    print("%02d:%02d:%02d" %(hrs, mins, test))
main()

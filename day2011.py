"""Day2011 by ศิษย์เทพปอง#2"""
def say(day, month):
    """Func. say for saying day"""
    lis = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dday = sum(lis[:month:])+day
    print('Friday' if dday%7 == 0 else 'Saturday' if dday%7 == 1 else\
    'Sunday' if dday%7 == 2 else 'Monday' if dday%7 == 3 else\
    'Tuesday' if dday%7 == 4 else 'Wednesday' if dday%7 == 5 else\
    'Thursday')
say(int(input()), int(input()))
     
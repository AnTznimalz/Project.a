"""
Numdays
"""
def main(day1, mon1, day2, mon2):
    """ Caluculate diff between 2 date """
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day1 > month[mon1] or day2 > month[mon2]:
        print('Impossible')
    else:
        day_1, day_2 = sum(month[:mon1])+day1, sum(month[:mon2])+day2
        print(abs(day_1-day_2))
main(int(input()), int(input()), int(input()), int(input()))

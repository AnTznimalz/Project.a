'''BloodDonation'''
def blood():
    '''Func. blood for finding who can donate blood'''
    age = int(input())
    weigh = int(input())
    time = int(input())
    message = 'Wow'
    if 17 < age < 60:
        if 45 <= weigh:
            if (time == 0 and age <= 55) or time > 0:
                message = 'Yes'
            else:
                message = 'No'
        else:
            message = 'No'
    elif age == 17 or 60 <= age <= 70:
        if 45 <= weigh:
            if (time == 0 and age <= 55) or time > 0:
                book = input()
                message = 'Yes' if book == 'True' else 'No'
            else:
                message = 'No'
        else:
            message = 'No'
    else:
        message = 'No'
    print(message)
blood()

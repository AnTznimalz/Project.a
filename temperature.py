'''Temperature'''
def cal():
    '''Func. cal for calculating'''
    ans = cel(temp=float(input()), type_a=input())
    final = oth(ans, type_b=input())
    print('%.2f'%final)
def oth(temp, type_b):
    '''Func. oth for changing celcius to other temp'''
    if type_b == 'F':
        temp = temp*(1.8)+32
        return temp
    if type_b == 'K':
        temp = temp + 273.15
        return temp
    if type_b == 'R':
        temp = (temp + 273.15)*1.8
        return temp
    else:
        return temp
def cel(temp, type_a):
    '''Func. cel for changing other temp to celcius'''
    if type_a == 'F':
        temp = (temp-32)/1.8
        return temp
    if type_a == 'K':
        temp = temp - 273.15
        return temp
    if type_a == 'R':
        temp = (temp/1.8)-273.15
        return temp
    else:
        return temp
cal()

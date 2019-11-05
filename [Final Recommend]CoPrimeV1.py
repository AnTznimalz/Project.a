'''[Final Recommend]CoPrimeV1'''
def coprime(num_a=int(input()), num_b=int(input())):
    '''Func. coprime for saying that 2 nummbers are co-prime or not'''
    begin = min(num_a, num_b)
    cop = 1
    for i in range(begin, 0, -1):
        if  num_a % i == 0 and num_b % i == 0:
            cop = i
            break
    if begin == 0:
        cop = max(num_a, num_b)
    print("YES" + '\n' + str(cop) if cop == 1 else "NO" + '\n' + str(cop))
coprime()

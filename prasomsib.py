'''PrasomSib'''
def nub(text, count):
    '''Func. nub for counting how many methods can sum of the near digits equal to 10'''
    for i in range(2, min(len(text)+1, 11)):
        for j in range(len(text) + 1 - i):
            count += 10 == sum([int(k) for k in text[j:j+i]])
    print(count)
nub(input(), 0)

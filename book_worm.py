'''Book_Worm'''
def book():
    '''Func. book for find the most book that you can read in time'''
    test = int(input())
    box = []
    max_book = 0
    for _ in range(test):
        time = float(input())
        books = int(input())
        for _ in range(books):
            box.append(int(input()))
            box.sort()
        for i in box:
            if i <= time:
                time -= i
                max_book += 1
        print(max_book)
        max_book = 0
        box = []
book()
       
def work():
    """Func. work for return name of card"""
    wanted_num = int(input())
    num_card = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    card = ['C', 'D', 'H', 'S']
    box = []
    for i in card:
        for j in num_card:
            box.append(j+i)
    print(box[wanted_num])
work()

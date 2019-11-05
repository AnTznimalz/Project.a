"""Black Jack Mor Pee Zad"""
def count(number):
    """Function count for counting score"""
    score, count_a = 0, 0
    for _ in range(number):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            card = "10"
            card = int(card)
            score += card
        elif card == "A":
            count_a += 1
        else:
            card = int(card)
            score += card
    while count_a != 0:
        if count_a == 1:
            if score + 11 > 21:
                score += 1
                break
            else:
                score += 11
                break
        elif count_a == 2:
            if score + 12 > 21:
                score += 2
                break
            else:
                score += 12
                break
        elif count_a == 3:
            score += 13
            break
    print(score)
count(int(input()))

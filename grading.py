""" Grading Student """
def grade():
    """ Func. grade for grading the student """
    for _ in range(int(input())):
        score = int(input())
        remain = score % 10
        if  0 < remain < 5 and score >= 38:
            goal = score - remain + 5
            if goal - score < 3:
                print(goal)
            else:
                print(score)
        elif remain < 10 and score >= 38:
            goal = score - remain + 10
            if goal - score < 3:
                print(goal)
            else:
                print(score)
        else:
            print(score)
grade()

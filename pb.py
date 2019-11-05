"""Plan B"""
def score():
    """Func.Score"""
    point = float(input())
    if point >= 450:
        return passing()
    else:
        return fail()
def passing():
    """Func.Pass"""
    print("Pass")
    prt()
def fail():
    """Func.Fail"""
    print("Fail")
    prt()
def prt():
    """Func prt"""
    print("Process is terminated")
score()

"""Oh! my score"""
def main():
    """Main Func."""
    score_1 = float(input())
    score_2 = float(input())
    score_3 = float(input())
    score_4 = float(input())
    score_5 = float(input())
    high = max(score_1, score_2, score_3, score_4, score_5)
    low = min(score_1, score_2, score_3, score_4, score_5)
    average = (score_1 + score_2 + score_3 + score_4 + score_5)/5
    print("MAX: %.2f" %high)
    print("MIN: %.2f" %low)
    print("AVG: %.2f" %average)
main()

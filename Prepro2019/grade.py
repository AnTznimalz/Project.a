"""00xx: Grade"""
def main():
    """Main Func."""
    score = float(input())
    if score < 0 or score > 100:
        print("Invalid Score.")
    else:
        if 80 <= score <= 100:
            print("A")
        elif 75 <= score < 80:
            print("B+")
        elif 70 <= score < 75:
            print("B")
        elif 65 <= score < 70:
            print("C+")
        elif 60 <= score < 75:
            print("C")
        elif 55 <= score < 60:
            print("D+")
        elif 50 <= score < 55:
            print("D")
        elif score < 50:
            print("F")
main()

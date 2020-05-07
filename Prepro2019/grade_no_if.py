"""Grade no if"""
def main():
    """Main Func."""
    num = float(input())
    g_1 = (80 <= num <= 100) * "A"
    g_2 = (75 <= num < 80) * "B+"
    g_3 = (70 <= num < 75) * "B"
    g_4 = (65 <= num < 70) * "C+"
    g_5 = (60 <= num < 65) * "C"
    g_6 = (55 <= num < 60) * "D+"
    g_7 = (50 <= num < 55) * "D"
    g_8 = (0 <= num < 50) * "F"
    print(g_1 + g_2 + g_3 + g_4 + g_5 + g_6 + g_7 + g_8)
main()

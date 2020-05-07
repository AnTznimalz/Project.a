"""00XX: Kaiju Lover"""
def main():
    """Main Func."""
    text = input()
    score = 0
    if "Godzilla"  in text and "KingGhidorah"  in text and\
         "Megalon"  in text and "Kamacuras" in text:
        score += 17
    elif "Godzilla"  in text and "KingGhidorah"  in text and "Megalon" in text:
        score += 8
    elif "Godzilla"  in text and "KingGhidorah" in text:
        score += 3
    elif "Godzilla"  in text:
        score += 1
    print("%d/17" %int(score))

main()

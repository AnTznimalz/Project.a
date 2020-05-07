"""Distance Between 2 points"""
def main():
    """Main Func."""
    pointx1, pointy1 = float(input()), float(input())
    pointx2, pointy2 = float(input()), float(input())
    distance = ((((pointx1-pointx2)**2)+((pointy1-pointy2)**2))**0.5)
    print("%.2f" %distance)
main()

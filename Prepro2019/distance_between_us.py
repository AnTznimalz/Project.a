"""Distance between us"""
def distance():
    """Distance Func."""
    town_a = float(input())
    town_b = float(input())
    town_c = float(input())
    a_b = abs(town_a-town_b)
    a_c = abs(town_a-town_c)
    b_c = abs(town_b-town_c)
    print("Distance between Town A and Town B = %.2f" %a_b)
    print("Distance between Town B and Town C = %.2f" %b_c)
    print("Distance between Town A and Town C = %.2f" %a_c)
distance()

"""00XX: Find Speed"""
import math
def main():
    """Func. Main"""
    distance = len(input())*2
    corner = math.radians(int(input()))
    speed_ini = float(input())
    high = distance*math.tan(corner)
    speed_fin = round((speed_ini**2 + 20*high)**0.5)
    print("Speed is %d m/s." %speed_fin)
main()

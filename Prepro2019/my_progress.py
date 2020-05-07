"""My Progress"""
def main():
    """Main Func."""
    name = input()
    distance = int(input())
    run = int(input())
    per = run/distance * 100
    print("%s วิ่งได้ %d%% แล้ว" %(name, per))
main()
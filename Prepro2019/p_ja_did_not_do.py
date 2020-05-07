"""P'Ja didn't do anything."""
def main():
    """Main Func."""
    name = input()
    logic = int(name == "Ja" or name == "Nunja" or name == "Nj")
    print(logic * "P'Ja didn't do anything.", end="")
    print(int(not logic) * ("P'%s might not be an innocent." %name))
main()

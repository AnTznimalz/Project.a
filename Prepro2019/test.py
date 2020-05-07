""" Test """
def main():
    """ Main Func. """
    txt = input()
    print(txt.title())
    for i in txt.title():
        if i.isupper():
            print(i + '.', end="")
main()
# def main():
#     """ Main Func. """
#     txt = input()
#     msg = ""
#     stack = 0
#     for i in range(len(txt)):
#         if i == 0:
#             msg += txt[i].upper()
#         else:
#             if txt[i] == ' ':
#                 stack = 1
#                 msg += txt[i]
#             else:
#                 if stack:
#                     msg += txt[i].upper()
#                     stack = 0
#                 else:
#                     msg += txt[i].lower()
#     print(msg)
#     for i in (msg):
#         if i.isupper():
#             print(i + '.', end=" ")
# main()

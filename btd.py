"""Breach The Door"""
def decode(sentence, newbox):
    """Func. decode for decoding this problem"""
    box = sentence.split(" ")
    for i in box:
        if len(i) > 6:
            if i.isalpha():
                newbox.append(i)
            elif i.isalnum():
                newbox.append(i.replace("0", "").replace("1", "").replace("2", "").replace("3", "")\
                .replace("4", "").replace("5", "").replace("6", "").replace("7", "")\
                .replace("8", "").replace("9", ""))
            else:
                text = ''
                for j in i:
                    if j.isalpha():
                        text += j
                    else:
                        j = ''
                        text += j
                newbox.append(text)
    for i in newbox:
        if len(i) > 6:
            if i.isalpha():
                print(i, end=" ")
decode(input(), [])

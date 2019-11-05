'''[Final Recommend]Classify'''
def classify():
    '''Func. classify for classifying student'''
    box, stu_dic = [], {}
    #create list of student
    while 1:
        stu_id = input()
        if stu_id == 'END':
            break
        box.append(stu_id)
    box.sort()

    #create keys in dic
    for i in box:
        wow = i[:4]
        if wow not in stu_dic:
            stu_dic[wow] = 1
        else:
            stu_dic[wow] += 1

    #print output
    text = ''
    for j in sorted(stu_dic):
        year, fac = j[:2], j[2:4]
        if year != text:
            print(year, int(fac), stu_dic[j])
        else:
            print('--', int(fac), stu_dic[j])
        text = year
classify()

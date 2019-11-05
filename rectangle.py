'''Rectangle_Area'''
def rec():
    '''Func. rec for calculating of 2 rectangles area'''
    rec_1 = input().split()
    rec_2 = input().split()
    wide_1 = abs(int(rec_1[0]) - int(rec_1[2]))
    high_1 = abs(int(rec_1[1]) - int(rec_1[3]))
    wide_2 = abs(int(rec_2[0]) - int(rec_2[2]))
    high_2  = abs(int(rec_2[1]) - int(rec_2[3]))
    
    #rec_1 (4 corners)
    pos_1a = rec_1[0], rec_1[1]
    pos_2a = rec_1[0], rec_1[1] + high_1
    pos_3a = rec_1[0] + wide_1, rec_1[1] + high_1
    pos_4a = rec_1[0] + wide_1, rec_1[1]

    #rec2 (4 corners)
    pos_1b= rec_2[0], rec_2[1]
    pos_2b= rec_2[0], rec_2[1] + high_2
    pos_3b= rec_2[0] + wide_2, rec_2[1] + high_2
    pos_4b= rec_2[0] + wide_2, rec_2[1]

    #area rec_1
    area_1 = wide_1*high_1

    #area rec_2
    area_2 = wide_2*high_2
rec()

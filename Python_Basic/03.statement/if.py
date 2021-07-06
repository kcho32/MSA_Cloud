def if_true():
    if 1:
        print('1은 참'
        )

    if 'aaa':
        print('str도 참')

    if 0:
        print('0은? 거짓')

    if True:
        print('bool도 쓰임')
    return


def days_31():
    month = int(input('몇월이 궁금하십니까?'))

    if month == 2:
        print('{0}월은 28일까지 있습니다.'.format(month)) 
    elif month < 8:
        if month % 2 == 1:
            print('{0}월은 31일까지 있습니다.'.format(month))
        elif month %2 == 0:
            print('{0}월은 30일까지 있습니다.'.format(month))
        else:
            print('{0}월은 존재하지 않습니다.'.format(month))
    elif month >= 8:
        if month <= 12:
            if month % 2 == 1:
                print('{0}월은 30일까지 있습니다.'.format(month))
            elif month %2 == 0:
                print('{0}월은 31일까지 있습니다.'.format(month))  
        else:
            print('{0}월은 존재하지 않습니다.'.format(month))
    return

        
days_31()
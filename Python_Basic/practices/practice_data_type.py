def average(grades_in_dict):
    total_grade = 0
    for course in grades_in_dict.keys():
        total_grade += grades_in_dict[course]

    return total_grade/len(grades_in_dict)


def even_odd(number):
    if number % 2 == 1:
        return 'odd'
    elif number %2 == 0:
        return 'even'


def sex(pin_str):
    numbers_list = pin_str.split("-")
    return int(numbers_list[1][0])


def collon_to_sharp(string):
    return string.replace(":","#")


def reversing_order(list1):
    list1.sort(reverse = True)
    #.sort()는 출력값이 None이다. 이 함수는 본 리스트를 수정하는 것이기 때문에
    #본 리스트를 리턴하면 된다.
    return list1


def joining_list(list1):
    return " ".join(list1)


def add_in_tuple(tuple1, tuple2):
    tuple3 = tuple1+tuple2
    print(id(tuple3),id(tuple1),sep="\n")
    #튜플은 수정이 안되기 때문에 새로운 주소에다 입력된 것이다.
    return tuple1 + tuple2


def why_no_list_for_key():
    return print("""
    리스트는 값이 변화 할 수 있기 때문에 key가 될 수 없다.
    따라서 3번만이 에럴를 일으킨다.
    """)


def pop_b_from_a(dic,key):
    #해당 함수 실행 시, dic에서 key와 그 value는 사라진다
    return dic.pop(key)


def eliminate_duplicates(lists):
    return list(set(lists))


def q12():
    a = b = [1,2,3]
    print('a: {0}\nb: {1}에서 a[1] = 4를 하면'.format(a, b))
    a[1] = 4
    print('a: {0}\nb: {1}가 나온다'.format(a, b))
    print('a와 b는 같은 메모리 주소를 공유하는 완전 동일 객체이기 때문이다')
    return


grades = {'국어': 80, '영어': 75, '수학': 55}
num = 13
pin = '881120-1068234'
a = "a:b:c:d"
q6 = [1, 3, 5, 4, 2]
q7 = ['Life', 'is', 'too', 'short']
q8_1 = (1,2,3)
q8_2 = (4,) #값이 하나만 있을시 ,를 붙여 튜플이라는 것을 명시한다
q10_1 = {'A':90, 'B':80, 'C':70}
q10_2 = 'B'
q11 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

#print(average(grades))
#print(even_odd(num))
#print(sex(pin))
#print(collon_to_sharp(a))
#print(reversing_order(q6))
#print(joining_list(q7))
print(add_in_tuple(q8_1,q8_2))
#print(why_no_list_for_key())
#print(pop_b_from_a(q10_1,q10_2))
#print(eliminate_duplicates(q11))
#q12()


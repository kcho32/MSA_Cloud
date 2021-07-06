<<<<<<< HEAD
=======
import sys
>>>>>>> daf597275073efc36eeed9af75c71d3292637138

def is_odd(integer):
    if integer % 2 == 1:
        answer = True
    else:
        answer = False

    return print('{0}은(는) 홀수입니까? : {1}'.format(integer,answer))


#average = lambda *args : sum(args)/len(args)


def addition():
    input1 = int(input("첫번째 숫자를 입력하세요:"))
    input2 = int(input("두번째 숫자를 입력하세요:"))

    total = input1 + input2
    print("두 수의 합은 %s 입니다" % total)


'''print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") ->이것만 띄어쓰기
print("".join(["you", "need", "python"]))'''


def read_write(text):
    f1 = open(text, 'w')
    f1.write('Life is too short.')
    f1.close()

    f2 = open(text,'r')
    print(f2.read())
    f2.close()


def write_add():
    f1 = open('test.txt','a')
    data = input("추가하실 문구는?\n")
    f1.write('\n' + data)
    f1.close()


def replace_txt(text):
    with open(text,'r') as f:
        data = f.read()
    data.replace("java","python")
    print(data.replace('java','python'))
    return 



#print(average(1,2,3,4,5,6,7,8,9))
#is_odd(3)
#addition()
#read_write('test.txt')
#write_add()
<<<<<<< HEAD
replace_txt('c:/cloud_msa/PYTHON_WORKSPACE/Python_Basic/practices/test.txt')
=======
replace_txt('c:/cloud_msa/PYTHON_WORKSPACE/Python_Basic/03.example/test.txt')
>>>>>>> daf597275073efc36eeed9af75c71d3292637138

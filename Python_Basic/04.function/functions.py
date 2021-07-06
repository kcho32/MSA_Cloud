global_variable = 10

def function1():
    local_variable = 10
    global global_variable
    global_variable += 10
    print("local variable: {0}\tglobal_variable: {1}".format(local_variable,global_variable))


def function2():
    local_variable = 100
    global global_variable
    global_variable += 10
    print("local variable: {0}\tglobal_variable: {1}".format(local_variable,global_variable))


def add_many(*num, sum = 0):
    for i in num:
        sum += i
    return print(sum)


function1()
#global variable을 수정해서 function 이후의 global_variable은 20이 된다
function2()
#flobal variable before function 1 != after funcion 1
add_many(1,2,3,4,5)
add = lambda a,b : a+b
print("lambda function{0}".format(add(3,4)),type(add))
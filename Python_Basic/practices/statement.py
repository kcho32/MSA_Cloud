def q1():
    a = "Life is too short, you need python"

    if "wife" in a: print("wife")
    elif "python" in a and "you" not in a: print("python")
    elif "shirt" not in a: print("shirt")
    elif "need" in a: print("need")
    else: print("none")
    return


def q2():
    count = 0
    answer = 0
    while count <= 1000:
        count += 1
        if count % 3 == 0:
            answer += count
    return answer


def q3():
    for i in range(5):
        print('*'*(i+1))


def q4():
    for i in range(100):
        print(i+1)


def q5():
    grades = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    answer = 0
    for i in range(len(grades)):
        answer += grades[i]
    return print(answer/len(grades))


def q6():
    numbers = [1, 2, 3, 4, 5]
    result = [n*2 for n in numbers if n%2 ==1]
    return print(result)


#q1()
#print(q2())
#q3()
#q4()
#q5()
q6()


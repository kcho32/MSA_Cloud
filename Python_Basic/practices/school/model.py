class person():
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)


    def info(self):
        print("\t이름: {0}\n\t나이: {1}\n\t".format(self.name, self.age), end = "")


class student(person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        super().info()
        print("전공: {0}".format(self.major))


class instructor(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def info(self):
        super().info()
        print("과목: {0}".format(self.subject))


class employee(person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def info(self):
        super().info()
        print("부서: {0}".format(self.department))

'''kw = student('조규원',28,"물리")
kd = instructor('홍길동', 40, '수학')
gd = employee('김개똥', 32, 'CS부서')
'''
'''people = [student('조규원',28,"물리"), student('조규투',30,"수학"), 
        student('조규삼',23,"만화"),instructor('홍길동', 40, '수학'),
        instructor('홍길금', 40, '파이썬'),instructor('홍길은', 40, '수학'),
        employee('김개똥', 32, 'CS부서'),employee('최개똥', 30, 'CE부서')]'''


'''kw.info()
kd.info()
gd.info()
'''

'''
for human in people:
    print("정보: ")
    human.info()'''
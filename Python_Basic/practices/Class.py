'''요구사항:
    1. 이름(name)
    2. 나이(age)
    3. 전공(major)
    정보 리턴

    student_info()

    instructor_info()
    1. 이름
    2. 나이
    3. 과목

    직원
    employee_info()
    department 추가

    specialization: 부모에서 자식 하나 더 뽑는 것
    상속은 generalization

    사용자 코드 (user) person : 자식마다 다른 사용법 -> 불편
    override 기능 이용
    
    설계:   부모 : 이름 나이 Person()
            자식 : 전공, 과목

    

'''

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
people = [student('조규원',28,"물리"), student('조규투',30,"수학"), 
        student('조규삼',23,"만화"),instructor('홍길동', 40, '수학'),
        instructor('홍길금', 40, '파이썬'),instructor('홍길은', 40, '수학'),
        employee('김개똥', 32, 'CS부서'),employee('최개똥', 30, 'CE부서')]


'''kw.info()
kd.info()
gd.info()
'''

for human in people:
    print("정보: ")
    human.info()
class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        phrase = "ID: {0}\n이름: {1}\n".format(self.id, self.name)
        return phrase
    

class Student(Person):
    def __init__(self, id, name, major):
        super().__init__(id, name)
        self.major = major

    def info(self):
        phrase =super().info() + "전공: {0}\n".format(self.major)
        return phrase


class Instructor(Person):
    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject

    def info(self):
        phrase =super().info() + "과목: {0}\n".format(self.subject)
        return phrase


class Employee(Person):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department

    def info(self):
        phrase =super().info() + "부서: {0}\n".format(self.department)
        return phrase



if __name__ == "__main__":
    kw = Student("kwdc", "조규원", "물리") 
    print(kw.info())
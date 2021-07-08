#menu display
from school.models import Student, Instructor, Employee


def menu_display():
    print("====== 인사관리 시스템 ======")
    print("1. 전체 목록 보기")
    print("2. 등록")
    print("3. 수정")
    print("4. 삭제")
    print("5. 상세보기")
    print("0. 종료")


#submenu display
def submenu():
    print("1. 학생정보")
    print("2. 강사정보")
    print("3. 직원정보")
    print("4. 처음으로 돌아가기")


#menu select
def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return menu


#message display
def message_display(message):
    print(message)


#list display
def list_display(people):
    print("=== 전체 목록 ===")
    for person in people:
        print(person.info())


#register person input
def input_display(type):
    id = input("아이디: ")
    name = input("이름: ")
    if type == "1":
        major = input("전공: ")
        return Student(id, name, major)
    elif type == "2":
        subject = input("과목: ")
        return Instructor(id, name, subject)
    elif type == "3":
        department = input("부서: ")
        return Employee(id, name, department)
    

def update_input_display(type, id):
    name = input("이름: ")
    if type == "1":
        major = input("전공: ")
        return Student(id, name, major)
    elif type == "2":
        subject = input("과목: ")
        return Instructor(id, name, subject)
    elif type == "3":
        department = input("부서: ")
        return Employee(id, name, department)       


#수정하거나 삭제 또는 상세보기를 위한 id 입력
def id_input_display(command):
    id = str(input("{0} id를 입력하세요.".format(command)))
    return id


#person display
def person_display(person):
    print("=== 상세 정보 ===")
    print(person.info())
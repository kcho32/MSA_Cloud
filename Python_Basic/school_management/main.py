from school.models import Employee, Instructor, Student
from school.exception import DuplicateError, NotFoundError
from school.templates import menu_display, menu_select, list_display, submenu, input_display, message_display, id_input_display, update_input_display, person_display
from school.views import get_all_people, register, get_person, update, remove, save_list, load_list

load_list()

while True:
    menu_display()
    menu = menu_select()

    if menu == "0":
        #종료
        save_list()
        message_display("인사시스템을 종료합니다.")
        break
    
    elif menu == "1":
        #전체 목록 보기: view.py에서 get_all_people() 인사목록 받아서
        #template에 list_display로 출력
        people = get_all_people()
        list_display(people)    

    elif menu == "2":
        #등록 submenu로 입력 받고 register(객체) 호출
        #DuplicateError 처리
        submenu()
        sub_menu = menu_select()
        if sub_menu == "1" or sub_menu == "2" or sub_menu == "3":
            person = input_display(sub_menu)
            try:
                register(person)
                message_display(person.id + "등록 성공")
            except DuplicateError as error:
                message_display(person.id + error)
        elif sub_menu == "4":
            break
        else:
            print("sub menu 1, 2, 3, 4 중 선택")
            
    elif menu == "3":
        #수정 id 입력 받고 get_person(id)로 검색 person 타입에 따라 수정정보 
        #입력 받고 view의 update(person)
        #NotFoundError 처리    

        mod_id = id_input_display("수정")

        try:
            person = get_person(mod_id)
            type = ""
            if isinstance(person, Student): type = "1"
            elif isinstance(person, Instructor): type = "2"
            elif isinstance(person, Employee): type = "3"
            mod_person = update_input_display(type, mod_id)
            update(mod_person)
            message_display(person.id + "수정 성공")
        except NotFoundError as error:
            message_display(person.id + error)

    elif menu == "4":
        #삭제 id 입력 받고 view의 remove(id)호출
        # #NotFoundError 처리   
        del_id = id_input_display("삭제")
        
        try:
            remove(del_id)
            message_display(del_id+" 삭제 성공")

        except NotFoundError as error:
            message_display(error)
        

    elif menu == "5":
        #상세 보기 id 입력 받고 views의 etPerson(id) 호출
        #person_display(person) 호출
        # NotFoundError 처리   
        search_id = id_input_display("검색")

        try:
            person =get_person(search_id)
            person_display(person)
                  
        except NotFoundError as error:
            message_display(error)
        

    

    else:
        message_display("1,2,3,4,5,0 번 중 선택하세요")
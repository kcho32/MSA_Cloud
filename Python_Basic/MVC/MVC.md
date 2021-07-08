# MVC(Mode View Controller) Pattern Architenture Terms
## MTV(Model Template View)는 같다 --Python
MVC의 View == MTV의 Template

                Model(xxxService, xxxRepository, xxxDao)
              Business Logic Encapsulation
              Persistance Business Logic Encapsualtion
              Data(xxxDTO, xxxEntity, xxxVO)-models.py





View(Template)-template패키지     Controller(View)-views.py
입력화면                               입력값 검증
data display(jsp, asp)                business logic 호출
                                      일정범위에 데이터 저장
                                      view select

class Calculator:
    def __init__(self):
        self.result = 0
        print("Calculator 생성자 호출!")
    
    def add(self, num):
        self.result += num
        return self.result
    

cal1 = Calculator()
#call back 안에서 상황에 맞았을 때 해당 메소드를 알아서 부른다
#self.result = 0
cal2 = Calculator()
#생성자를 이용해서 instance화 cal1,2라는 객체(object) 생성
#self.result = 0

print(cal1.add(3), cal2.add(4),sep = "\n")
#3, 4
print(cal1.add(3), cal2.add(4),sep = "\n")
#6, 8
print(cal1.add(3), cal2.add(4),sep = "\n")
#9, 12

#Car 추상화 attribute(member variable), operator(member method)
class Car:
    def __init__(self, name, cc, color):
        self.name = name
        self.cc = cc
        self.color = color
    

    def car_info(self):
        print('{0} 기종의 차는 {1}색의 배기량 {2}CC입이다'.format(self.name,self.color,self.cc))

#객체 생성(instance화) 및 초기화 : 생성자
ckw = Car('부가티 베이론', 1000, '검정')

#객체 기능 사용
ckw.car_info()

#상속을 하려면 괄호 안에 넣으면 된다
#: 부모 클래스(Super class)의 master variable과 member method를
#자삭 클래스(Sub Class)에서 사용 가능하도록 허용
#Super Class에 초기화 메서드가 있으면 서브에선 안쓰고 부모꺼 불라와서 사용 가능


class Calculator2(Calculator):
    def __init__(self):
        super().__init__()
        print("sub 생성자 호출!")


    def add(self, num):#만약 부모와 자식 둘다 같은 이름의 메서드가 있다면
        return num     #자식 것이 응답 되게 할 수 있다
        

    def sub(self, num):
        self.result -= num
        return self.result

cal3 = Calculator2()
print(cal3.add(3))
print(cal3.add(3))
print(cal3.sub(1))
'''
사용자 정의 Exception
1. Exception Class 정의(Exception 상속)
2. 사용자가 원하는 조건이 발생 되었을 때 Exception발생 
    (raise 사용자 정의 Exception() )
3. 사용 코드에서 try-except-final로 

'''

class UserException(Exception):
    def __init__(self, message):
        self.message = message
    
    
    def get_message(self):
        return self.message
    
    def __str__(self):
        return self.message

def exception_f(nick):
    if nick == "바보":
        raise UserException("사용자 정의 예외입니다.")
    print(nick)

try:
    exception_f('바보')

except UserException as m:
    print(m.get_message())
    print(m)
    print("나쁜 말입니다")



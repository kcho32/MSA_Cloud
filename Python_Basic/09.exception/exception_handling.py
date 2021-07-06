'''
예외처리
try:
    예외발생 가능한 실행문

except:
    예외발생 시 실행문

else:
    예외 발생 안했을 때 실행문

finally:
    예외 발생과 상관 없이 무조건 실행문

*try 이후에는 무조건 except나 finally가 필요하다
*멀티 예외 처리는 except를 여러개 쓰면 된다

try:
    예외발생 가능한 실행문1
    예외발생 가능한 실행문2

except 예외타입 as 오류메시지1 변수:
    예외발생 시 실행문

except 예외타입 as 오류메시지2 변수:
    예외발생 시 실행문2

except 예외타입 as 오류메시지3 변수, 오류메시지4 변수:
    예외발생 시 실행문2



'''


try:
    datas = [1,2,3]
    print(datas[3]) #index error
    datas[1]/0
except (IndexError, ZeroDivisionError) as a:
    print(a)

else:
    print("왠일로 에러가 없니?")

finally:
    print("에러는 겨우 넘겼다 진짜")


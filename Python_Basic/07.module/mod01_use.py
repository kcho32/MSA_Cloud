#모듈: 독립적인 기능을 위한 변수, 함수, 클래스를 모아 놓은 파일
#다른 모듈의 기능 사용:     import 모듈이름
#                     또는 from 모듈이름 import 함수리스트



#import mod01
#print("10 + 20 = {0}".format(mod01.add(10, 20)))
#print("20 - 10 = {0}".format(mod01.add(20, 10)))
#전체를 불러오면 함수 앞에 이름.함수()


from mod01 import add
print("10 + 20 = {0}".format(add(10, 20)))
#하나만 불러오면 안써도 된다.
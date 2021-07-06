def add(a,b):
    return a+b


def sub(a,b):
    return a-b

#print(__name__) #__name__ module 이름을 의미한다 근데 실행파일이 해당 모듈이면 main이 출력
#현재 이 파일을 실행시 __name__은 __main__이다
#다른 파일을 통해 이 파일을 불러온다면 __name__은 mod01이 되는 것이다.

#따라서 테스트를 할때만 코드가 돌아가게 하려면
if __name__ == "__main__":
    print("testing working?")
    print("{0}".format(add(1,2)))

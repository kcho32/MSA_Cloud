# for문은 반복 횟수 정해져 있는 루프를 만들때
# while문은 특정 조건을 정해두고 만족할때까지 무한적으로 루프 돌린다


def count10():
    count = 0
    while True:
        count += 1
        print(count)
        if count == 10:
            print('loop를 종료합니다.')
            break
    return


def use_continue():
    floor = 2*int(input('몇겹의 트리을 쌓겠습니까?'))
    count = 0
    while count != floor:
        count += 1
        if count % 2 == 0:
            continue
        print(' '*((floor//2-count//2)-1),'*'*count,sep= "")


def nine_nine():
    for i in range(1,10):
        for j in range(2,10):
            print(i*j,end = "\t")
        print(' ')



#use_continue()
nine_nine()
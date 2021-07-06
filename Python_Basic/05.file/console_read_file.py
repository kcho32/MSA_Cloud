#키보드 입력 -> 파일 쓰기

f = open("test.txt", 'w')

#data = input("keyboard input: ")
#f.write(data)

while True:
    data = input('keyboard: ')
    if not data : break
    f.write(data+"\n")

f.close()
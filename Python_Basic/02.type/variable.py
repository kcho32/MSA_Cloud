from copy import copy

a = [1,2,3,4]
b = a
print(id(a))
print(id(b))

print( a is b)
#같은 주소
c = [1,2,3,4]
d = c[:]
e = copy(c)
print(id(c))
print(id(d))
print(id(e))
#다른 주소
print(c is d)

a.append(7)
print(b)# a에 7을 추가해도 b에도 추가됨

c.append(7)
print(d)# c에는 추가해도 d는 안바뀜


#is는 아얘 같은 것이냐고 물어보는 것 (주소 또한)
#같을 때 a를 바꿀시 b도 같이 바뀐다
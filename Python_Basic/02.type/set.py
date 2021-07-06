#집합은 리스트와 달리 중복이 안된다.
#순서도 랜덤?

s1 = set([1,3,4,5,6])
s2 = set([3,1,2,2,3,3])
print(s1,s2,sep = "\n")

s3 = s1|s2
print(s3)

s4 = s1.union(s2)
print(s4)

if s1.intersection(s2) == s1&s2:
    print(s1.intersection(s2))

if s1.difference(s2) == s1-s2:
    print(s1.difference(s2))

s5 = set("organization")
print(s5)

print("교집합: {0}".format(s1.intersection(s2)))
print("합집합: {0}".format(s1.union(s2)))
print("차집합: {0}".format(s1.difference(s2)))

s1.add(7)
print(s1)
s1.remove(6)
print(s1)
s1.update(s2)
print(s1)

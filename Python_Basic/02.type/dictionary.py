#key값과 value값으로 주어짐
#key should never be duplicated
#key값이 index대신 쓰인다고 생각하면 편할 듯

dic = {"Name":"Kyuwon Cho","Age":28,"Sex":"Male","Major":"Physics"}
print(dic)

dic['School'] = 'UIUC'
print(dic)

dic['Age'] = 27
print(dic)

dic2 = {"Name":"Kyuwon Cho","Age":28,"Sex":"Male","Major":"Physics",'Major':"Phys"}
print(dic2)

del dic['Major']
print(dic)

print("이름: {0}".format(dic['Name']),"나이: {0}".format(dic['Age']),"성별: {0}".format(dic['Sex']),sep = "\n")
print("이름: {0}\n나이: {1}\n성별: {2}".format(dic['Name'],dic['Age'],dic['Sex']))

#dictionary key list
print(dic.keys())

for key in dic.keys():
    print('key: {0}, value: {1}'.format(key, dic.get(key)))
    print('key: {0}, value: {1}'.format(key, dic[key]))

#dictionary (key:value) list
a = dic.items()
b = []
for i in a:
    b.append(i)
#print(b)

cloud_msa = [
    {'name':"유민기", 'age': 27, "major": '컴공'},
    {'name':"김건우", 'age': 28,"major": '물리'},
    {'name':"조규원", 'age': 27, "major": '컴공'}
]
print(cloud_msa)
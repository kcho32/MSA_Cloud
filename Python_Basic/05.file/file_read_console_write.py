f = open('test.txt', 'r')

"""while True:
    data = f.readline()
    if not data : break
    print(data)"""

"""lines = f.readlines()
for line in lines:
    print(line)

f.close()"""

data = f.read()
print(data)
f.close()
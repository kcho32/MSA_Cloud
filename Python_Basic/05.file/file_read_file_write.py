f = open('C:/cloud_msa/PYTHON_WORKSPACE/Python_Basic/05.file/test.txt', 'r') #with open('test.txt','r') as f:   f.close()
fw = open('C:/cloud_msa/PYTHON_WORKSPACE/Python_Basic/05.file/test_copy.txt', 'w')

data = f.read()
f.close()
fw.write(data)


fw.close() #안하면 자원 낭비가 되어서 꼭 해주는게 좋다.

#close 안한 것을 대비해서 

f = open('test.txt', 'r')
fw = open('test_copy.txt', 'w')

data = f.read()
fw.write(data)

f.close()


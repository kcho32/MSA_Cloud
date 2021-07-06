'''
filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 
음수를 모두 제거해 보자.
'''

list_example = [1,-2, 3, -5, 8, -3]

answer = list(filter(lambda x: x>0, list_example))
print(answer)
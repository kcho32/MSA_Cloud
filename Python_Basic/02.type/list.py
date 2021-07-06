def find_length(a):
    print(len(a))
    return


def list_replace(list, index, value):
    answer = []
    answer.extend(list)
    answer[index] = value
    #주의 해야 될게 answer = list로 해버리면 answer를 수정해도 list까지 같이 수정이 되기 때문에
    #빈 리스트인 answer에 extend로 추가를 해서 해결했다. 내용은 같지만 연동 x
    return answer


def list_delete(list,index):
    answer = []
    answer.extend(list)
    del answer[index]
    return answer


def list_append(list, element):
    answer = []
    answer.extend(list)
    answer.append(element)
    return answer


def list_pop(list,index):
    answer = []
    answer.extend(list)
    answer.pop(index)
    return answer
    #index없으면 마지막 숫자 빠짐


a = [1,2,3,['a','b','c']]
print("a list 첫번째: {0}   두번째:{1}  세번째:{2}  네번째:{3}".format(a[0],a[1],a[2],a[3]))
print("4번 배열의 첫번째: {0}   두번쨰: {1} 세번째: {2}".format(a[3][0],a[3][1],a[3][2]))

b = [1,2,3,4,'a','b','c','d']

a_length = find_length(a)
list_after_replace = list_replace(b,3,1)
list_after_delete = list_delete(b,2)
list_after_append = list_append(b,'d')
list_after_pop = list_pop(b,0)



print(list_after_replace,list_after_delete,list_after_append,list_after_pop, sep = "\n")
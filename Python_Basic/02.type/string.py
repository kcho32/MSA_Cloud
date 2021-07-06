def str_add(str1, str2):
    print(str1 +" "+str2)
    print(str1 , str2, sep = " ")
    return


def str_types():
    a = 'hello world'
    b = 'say "hello world"'
    c = '''
    say "hello world"
    then you will get 'hello world'
    '''
    d = "I can use both \"double quatation\" and \'single quatation\' at once when using \"\\\" in front of \" and \'"

    print(a)
    print(b)
    print(c)
    print(d)
    return


def str_index(str,n,m):
    return print(str[n:m])


def string_format(number, string):
    print("I ate %d apples" %number)
    print("I hate %s." %string)
    '''
    %s: string -> 아무거나 다 가능
    %c: char
    %d: int
    %f: float
    %o: octa
    %x: hexa
    %% Literally %
    '''
    print("숫자 %s도 되고 문자열 %s도 된다" %(number,string))
    print("%10shello" %string)#총10글자 뒤로 정렬
    print("%-10shello" %string)#총 10글자 앞으로 정렬

    print("I ate {} apples".format(number))
    print("I ate {} aplles with {}".format(number,string))
    


    return 


def find_char(string,character):
    print(string.find(character),"find함수 사용시 없다면 -1",sep = " ")
    print(string.index(character),"index함수는 없으면 에러",sep = " ")
    return 


def upper_case(string):
    return string.upper()


def lower_case(string):
    return string.lower()


def no_space(string):
    #왼쪽 공백을 제가하려면 lstrip, 오른쪽 공백 제거하려면 rstrip, 양쪽은 그냥 strip.
    return string.strip()


def str_split(string, char):
    return print(string.split(char))


def str_join(string1,element):
    #string1 사이에 element를 끼워 넣는데
    return print(element.join(string1))



head: str = "Python "
tail: int = 3.96
number = '0123456789'

#str_add(head, str(tail))
#str_index(number,0,len(number))
#string_format(3, "you")
#find_char("abcdefg","d")
#str_split(number,"3")
str_join(number,"1")


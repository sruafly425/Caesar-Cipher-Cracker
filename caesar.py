#caesar password
import requests
up=list()
down=list()
up=up[:28]
down=down[:28]
print("▶  시저 암호 해독기 v 1.0\n 복호화할 암호를 임력하세요 ")
sen = input()
k = len(sen)
sen = sen[:k]
array = list()
FLAG = 0
for a in sen:
    array.append(a)
print("".join(array))
for s in range(0, 24, 1):
    modifarray = list()
    modifarray = modifarray[:k]
    for a in array:
        sums = ord(a)+1+s
        if (ord(a) == 32):
            modifarray.append(chr(32))
        elif (sums < 97):
            modifarray.append(chr(122-((97-sums)%26)))
        elif (sums > 122):
            modifarray.append(chr((sums-122)%26+96))
        else:
            modifarray.append(chr(sums))
    #dictionary search
    word = list()
    word = word[:k]
    
    for letter in modifarray:
        if (letter == ' '):
            try:
                url = 'https://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query={0}'.format("".join(word))
                response = requests.get(url=url)
                keyword = '<strong>{0}</strong></a>'.format("".join(word))
                if keyword in response.text:
                    up.append("".join(modifarray))
                else:
                    down.append("".join(modifarray))
                break
            except:
                up.append("".join(modifarray))
                FLAG = 1
        else:
            word.append(letter)
    print("".join(modifarray))
   
        
print("\n\n\n")
print(">> 가능성 높음")
print("\n")
if (FLAG == 1):
        print("!! 인터넷 연결이 없습니다. 분류 기능을 사용하시려면 인터넷에 연결하세요.\n")
print("\n".join(up))
if (FLAG == 0):
    print("\n\n\n>> 가능성 낮음")
    print("\n")
    print("\n".join(down))
    print("\n\n")

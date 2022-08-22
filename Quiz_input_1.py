# 문제 - 사용자에게 문장 1개를 입력받아서, 출력해주세요.

# print("""문장하나를 입력해주세요 : """, end = " ")    input 안에 문자열 입력 가능
from re import A


l = input("이름 입력해주세요 : ")
print(l)

# 응용 - 초등학생 수준의 수학문제

while True:
    a = input('1더하기 1은? : ')
    
    if a != '2':
        print('{}님, 혹시 미취학 아동이신가요?'.format(l))
        continue
    else:
        print('정답')
    break
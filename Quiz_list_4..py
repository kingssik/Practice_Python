# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 
# '화'가 리스트 안에 들어있는지 알려주세요.

a = ['월', '화', '수', '목', '금']

if '화' in a:
    print('Yes')
else:
    print('No')

# in 연산자의 결과는 bool 타입이며 확인하고자 하는 데이터가 있는 경우 True, 없는 경우 False를 반환
# not in 연산자의 경우 반대로 출력
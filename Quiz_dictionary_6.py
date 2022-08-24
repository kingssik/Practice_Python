# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, items()로 key, value 순회출력

lastday = {}
lastday['1월'] = 31
lastday['2월'] = 28
lastday['3월'] = 31

for key, value in lastday.items():
    print(key + " : " + str(value) + "일")
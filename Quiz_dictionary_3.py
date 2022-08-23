# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key 순회출력

month_end_days = {}
month_end_days["1월"] = 31
month_end_days["2월"] = 28
month_end_days["3월"] = 31

print('v1')
for key1 in month_end_days.keys():
    print(key1)

print('v2')
for key2 in month_end_days:
    print(key2)
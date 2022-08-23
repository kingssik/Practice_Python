# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key, value 순회출력

lastday = {}
lastday['1월'] = 31
lastday['2월'] = 28
lastday['3월'] = 31

print('v1')
for key in lastday:
    print('{}은 {}일까지'.format(key, lastday[key]))

print('v2')
for month in lastday.keys():
  end_day = lastday[month]
  print(month + "은 " + str(end_day) + "까지 있습니다.")
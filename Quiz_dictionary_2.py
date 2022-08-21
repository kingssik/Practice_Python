# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기

print('v1')
l = {}
l['1월'] = 31
l['2월'] = 28
l['3월'] = 31
l['4월'] = 30
l['5월'] = 31
l['6월'] = 30
l['7월'] = 31
l['8월'] = 31
l['9월'] = 30
l['10월'] = 31
l['11월'] = 30
l['12월'] = 31
print(l)

print('v2')
m = {}
for i in range(1,13):
    month = str(i) + '월'

    med = 31
    
    if i == 2:
        med = 28
    elif i in [4,6,9,11]:
        med = 30
    
    m[month] = med
print(m)

print('v3')

month_end_days = {}

month_end_days_list_ver = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for j, end_day in enumerate(month_end_days_list_ver):
    month = str(j+1) + '월'
    month_end_days[month] = end_day

print(month_end_days)
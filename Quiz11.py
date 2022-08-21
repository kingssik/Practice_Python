# 문제1 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력 len 사용
last = [31,28,31,30,31,30,31,31,30,31,30,31]

print('문제1')
for i in range(len(last)):
    print('{}월은 {}일까지'.format(i+1, last[i]))

# 문제2 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, enumerate 사용
print('문제2')
# v1
for j, k in enumerate(last, start = 1):
    print('{}월은 {}일까지'.format(j, k))
# v2
for l, last in enumerate(last):
  month = l + 1
  print("{}월은 {}일까지".format(month, last))
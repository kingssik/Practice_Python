# 문제 : for문으로 구구단 8단 출력
i=1
while i<=9:
  dan = 8
  print("{} * {} = {}".format(dan, i , dan*i))
  i+=1

dan = 8
for i in range(1, 10):
  print("{} * {} = {}".format(dan, i , dan*i))
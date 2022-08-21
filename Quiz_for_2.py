# 문제 : for문으로 1부터 100 사이의 짝수만 출력
# v1
for i in range(1,101):
    if i%2 == 0:
        print(i)
# v2
for j in range(2, 101, 2):
  print(j)

# 문제 : for문으로 100부터 1 사이의 짝수만 출력
# v1
for k in range(100,0,-1):
    if k%2 == 0:
        print(k)
# v2
for l in range(100, 0, -2):
  print(l)
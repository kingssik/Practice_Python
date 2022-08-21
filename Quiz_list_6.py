# 문제 : 1부터, 10까지 리스트로 묶어주세요
# 조건 : 정답을 여러가지 버전으로 만들어주세요.

def sol_v1():
  print("== 담기 ==")
  l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  print("== 출력 ==")
  print(l[0])
  print(l[1])
  print(l[2])
  print(l[3])
  print(l[4])
  print(l[5])
  print(l[6])
  print(l[7])
  print(l[8])
  print(l[9])

def sol_v2():
  print("== 담기 ==")
  l = [1, 2, 3, 4, 5, 6, 7]
  l.append(8)
  l.append(9)
  l.append(10)

  print("== 출력 ==")

  c = len(l)

  i = 0
  while i < c:
    print(l[i])
    i += 1

def sol_v3():
  print("== 담기 ==")
  l = []

  i = 1
  while ( i <= 10 ):
    l.append(i)
    i += 1

  print("== 출력 ==")

  for value in l:
    print(value)

print("== 정답 v1 ==")
sol_v1()
print("== 정답 v2 ==")
sol_v2()
print("== 정답 v3 ==")
sol_v3()
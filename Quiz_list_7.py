# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 
# 리스트에 있는 '금'을 삭제하는 3가지 방법을 보여주세요.

from re import L


l = ['월', '화', '수', '목', '금']

# v1
del(l[l.index('금')])
print(l)

l.append('금')
print(l)

# v2
l.remove('금')
print(l)

l.append('금')
print(l)

# v3
del(l[-1])  # 또는 del l[4]
print(l)
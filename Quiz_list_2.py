# 문제 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 
# 그리고 리스트 안에 있는 '오'를 제거해주세요.

a = [2, 1, '오', 6, 7]

# v1
del(a[a.index('오')])
print(a)

# v2
a.insert(2, '오')
print(a)
a.remove('오')
print(a)

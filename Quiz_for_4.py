# 문제 : for문으로 구구단 1단 ~ 9단 출력
for dan in range(1, 10):
    print('{}단'.format(dan))
    for i in range(1, 10):
        print('{} * {} = {}'.format(dan, i, dan*i))
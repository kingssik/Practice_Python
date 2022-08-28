# Quiz
# 리스트안에 있는 내용들을 text3.txt에 저장해주세요.
list1 = ["사과", "배", "딸기", "수박"]

file = open('text3.txt', 'w')
for i in list1:
    file.write(i + '\n')
file.close()
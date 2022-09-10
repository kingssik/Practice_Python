# 간단한 주소록 프로그램
names = []
homes = []

# array(배열) -> 데이터를 순서(index)로 관리 (리스트) -> 일괄처리
# map(맵) -> 데이터를 문자(key)로 관리 (딕셔너리) -> 구조화

user_list = []
# 파이썬에서 배열에 데이터 넣기 -> append

# 1. jason 데이터 저장
jason = {"name" : "jason", "home" : "New York"} # 맵
user_list.append(jason)

# 2. Chicago 사는 howard 저장
howard = {"name" : "howard", "home" : "Chicago"} # 맵
user_list.append(howard)

print("======= 주소록 =======")
for user in user_list :
    print("이름 : ", user["name"])
    print("주소 : ", user["home"])
    print("======================")
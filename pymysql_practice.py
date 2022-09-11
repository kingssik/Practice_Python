import pymysql as my

# connect
db = my.connect(
    host = 'localhost',
    user = 'root',
    password ='',
    charset = 'utf8'
)
cursor = db.cursor(my.cursors.DictCursor) # 넣으면 딕셔너리 형태로 select함(안 넣으면 튜플형태)
cursor.execute('USE addressBook;')

# INSERT
# cursor.execute('INSERT INTO address (`name`, home, regDate) VALUES ("Kang", "GUNSAN", NOW())')

# select 주의 : 항상 fetchall이나 fetch 계열 함수를 사용해야 한다.
# value = cursor.execute('SELECT * FROM address;')
# value = cursor.fetchall()
# print(value)
# print(value[0]["regDate"])

# update
# cursor.execute("UPDATE address SET home = 'Busan' WHERE `name` = 'lee'")

# execute() 후에는 commit하고 close 해줘야 한다
db.commit()
db.close()
import pymysql

# 使用PyMySQL连接MySQL
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'c.r/2003',
    database = 'baidu_competition'
)

# 创建游标对象
cursor = conn.cursor()

# 进行统计
# 执行查询过程
cursor.execute("select id from partial_clear_set where is_blurry=0")

# 获取查询结果
rows = cursor.fetchall()

cursor.close()
conn.close()

print(len(rows))
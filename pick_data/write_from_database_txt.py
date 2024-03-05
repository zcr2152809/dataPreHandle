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

# 执行查询过程
cursor.execute("select path,label from partial_clear_set where is_blurry=0")

# 获取查询结果
rows = cursor.fetchall()

# 写入到标签文件
f = open('../results/label_partial_clear_set.txt', 'w', encoding='utf-8')
for row in rows:
    one_line = row[0] + '\t' + row[1] + '\n'
    f.write(one_line)

# 关闭文件
f.close()

# 关闭数据库连接
cursor.close()
conn.close()
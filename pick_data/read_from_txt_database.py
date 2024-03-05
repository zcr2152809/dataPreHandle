import pymysql

# 使用PyMySQL连接MySQL
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'c.r/2003',
    database = 'baidu_competition'
)

# 定义一个空列表来保存图片路径和标签
dataset_info = []

# 使用with语句打开文件，这样可以确保文件在使用后会被正确关闭
with open('D://jingProjects//智能车竞赛//Baidu//OnlineCompetition//DataForCompetitor//DataForCompetitor//train_label.txt', 'r', encoding='utf-8') as file:
    # 遍历文件的每一行
    for line in file:
        # 使用strip方法去除可能的前后空白字符（包括换行符）
        stripped_line = line.strip()
        # 使用split方法分割路径和标签，假设它们之间用空格分隔

        path, label = stripped_line.split('\t')
        # 将路径和标签作为一个元组添加到列表中
        dataset_info.append((path, label))

# 创建游标对象
cursor = conn.cursor()

# 插入数据
for item in dataset_info:
    cursor.execute("INSERT INTO partial_clear_set (class, path, label) VALUES (%s, %s, %s)", (0, item[0], item[1]))
    conn.commit()

cursor.close()
conn.close()



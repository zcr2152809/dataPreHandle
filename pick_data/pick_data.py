import numpy as np
from joblib import load
from generate_pick_model import is_blurry_fuction
import cv2
import pymysql

# 使用PyMySQL连接MySQL
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'c.r/2003',
    database = 'baidu_competition'
)

# 加载模型
model = load('../tools/decision_tree_model_clear_part_blurry.joblib')

# 创建ndarray数组
array_test = np.array([[0., 0., 0., 0., 0., 0.]])

# 创建游标对象
cursor = conn.cursor()

# 执行查询过程
cursor.execute("select id,path from partial_clear_set")

# 获取查询结果
rows = cursor.fetchall()

count = 0
miss = 0
for row in rows:
    imagePath = 'D://jingProjects//smartCarCompetition//Baidu//OnlineCompetition//DataForCompetitor//DataForCompetitor//' + row[1]
    image = cv2.imread(imagePath)

    if image is None:
        miss = miss + 1
        cursor.execute("UPDATE partial_clear_set SET is_blurry = %s WHERE id = %s", (1, row[0]))
        continue

    array_test[0][0] = is_blurry_fuction.Canny(image)
    array_test[0][1] = is_blurry_fuction.contrast(image)
    array_test[0][2] = is_blurry_fuction.FFT(image)
    array_test[0][3] = is_blurry_fuction.frequency(image)
    array_test[0][4] = is_blurry_fuction.Laplacian(image)
    array_test[0][5] = is_blurry_fuction.SSIM(image)

    pred = model.predict(array_test)

    cursor.execute("UPDATE partial_clear_set SET is_blurry = %s WHERE id = %s", (pred[0], row[0]))

    if count % 100 == 0:
        print(count)
    count = count + 1

print('miss: {}'.format(miss))

conn.commit()

cursor.close()
conn.close()


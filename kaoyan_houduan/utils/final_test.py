import numpy as np
import csv
final_school = []
# 初始化院校矩阵
item_matrix = {}
def SchoolRecommend(school_info):
    with open('schoolinfo.csv', newline='', encoding='utf-8') as csvfile:
        # 创建CSV读取器对象
        reader = csv.reader(csvfile)
        # 读取文件的首行，即表头
        header = next(reader)
        # 遍历CSV文件的每一行
        for row in reader:
            # 将第一列作为键，其余列作为值
            item_name = row[0]
            properties = [int(x) for x in row[1:6]]
            # 将键值对添加到院校矩阵中
            item_matrix[item_name] = properties

    # 打印生成的院校矩阵
    # print(item_matrix)

    # 输入院校向量
    input_item_vector = np.array(school_info)
    print(input_item_vector,'输入向量')
        # 计算余弦相似度
    similarities = {item: np.dot(item_matrix[item], input_item_vector) / (
                    np.linalg.norm(item_matrix[item]) * np.linalg.norm(input_item_vector)) for item in item_matrix}
    print(similarities)
    k = 500
    most_similar_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]
    # most_similar_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

        # 输出结果
    print('最相似的结果:')
    for item_id, similarity in most_similar_items:
        # print('- 学校id {}: 相似度={}'.format(item_id, similarity))
        final_school.append(item_id)
    # print(len(final_school),final_school)
    # print(list(set(final_school)))
    return list(set(final_school))

import pymysql
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='pc',charset='utf8mb4')
cursor = conn.cursor()

# 查询岗位描述数据
query = "SELECT 岗位描述 FROM `qx`"
cursor.execute(query)
results = cursor.fetchall()

# 关闭数据库连接
cursor.close()
conn.close()

# # 将岗位描述合并为一个字符串
text = ' '.join([result[0] for result in results if result[0] is not None])
# print(text)
# 使用jieba进行中文分词
words = jieba.cut(text)

# 统计词频
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# 生成词云图
wordcloud = WordCloud(font_path='SimHei.ttf', width=800, height=400)
wordcloud.generate_from_frequencies(word_freq)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# 保存词云图到本地
wordcloud_image_path = './static/assets/img/word.png'
wordcloud.to_file(wordcloud_image_path)
print("词云图已保存到本地:", wordcloud_image_path)
# plt.show()

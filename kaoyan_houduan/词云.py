from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
# 读取文本文件
text="国山东网-感知山东5月2日讯(记者 刘自锐)5月1日，临沂市蒙阴萌乐世界景区以“萌乐世界·萌开了”为主题，为广大市民和游客献上了一场高标准的节庆游乐嘉年华。至此，在万众期待下，萌乐世界距正式开园又近了一步"

# 创建WordCloud对象，设置参数
wordcloud = WordCloud(width=800, height=600, background_color='white').generate(text)

# 配置词云
wc = WordCloud(font_path='msyh.ttc', width=800, height=600, background_color='white').generate(text)

# 绘制词云图像
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
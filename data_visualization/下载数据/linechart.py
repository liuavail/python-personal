#折线图绘制
import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
#设置主题样式
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_value,squares,linewidth = 3)

#设置图形标题并给坐标轴加标签
ax.set_title("Squares Numbers",fontsize = 24)
ax.set_xlabel("Value",fontsize = 14)
ax.set_ylabel("Square of Value",fontsize = 14)
#设置刻度标记的大小
ax.tick_params(labelsize = 14)

plt.show()
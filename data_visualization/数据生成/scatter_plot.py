#散点图绘制
import matplotlib.pyplot as plt 

x_values = range(1,1001)
y_values = [x**2 for x in range(1,1001)]
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

#设置每个坐标值的取值范围
ax.axis([0,1100,0,1100000])
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()
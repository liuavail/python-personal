from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('data_weather/death_valley_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

'''#查看首行元素及对应序号
for index,column_header in enumerate(header_row):
    print(index,column_header) '''

#提取最高温度
dates,highs,lows = [],[],[]
for row in reader:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Miss data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

#根据数据绘制图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha = 0.5)
ax.plot(dates,lows,color='blue',alpha = 0.5)
#给图表区着色
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha=0.1)
#绘制斜的日期标签
fig.autofmt_xdate()
#设置图形的格式
ax.set_title("Daily High and Low Temperatures,2018\n Death Valley",fontsize = 20)
ax.set_xlabel('',fontsize = 16)
ax.set_ylabel("Temperature(F)",fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
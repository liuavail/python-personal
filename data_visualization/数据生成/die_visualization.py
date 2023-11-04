from die import Die
import plotly.express as px

#创建一个D6
die_1 = Die()
die_2 = Die(10)

#掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_die_number = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_die_number+1)
for values in poss_results:
    frequency = results.count(values)
    frequencies.append(frequency)

#对结果可视化
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
#进一步定制图形
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual_d6d10.html')
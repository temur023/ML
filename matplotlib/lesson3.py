#pie charts
from matplotlib import pyplot as plt

plt.title('Pie chart')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0] #in order to emphasize
plt.pie(slices,labels=labels,explode=explode,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
plt.show()
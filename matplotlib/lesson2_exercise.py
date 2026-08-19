import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
customers = pd.read_csv('customers.csv')

merged = orders.merge(customers, how='inner',on='customer_id')
print(merged)

grouped = merged.groupby(['city','is_premium'])['total_price'].mean().unstack()

print(grouped.index)
x_position = np.arange(len(grouped.index))

plt.bar(x_position ,grouped[True],width=0.25, label='Premium users',color='b')
plt.bar(x_position + 0.25, grouped[False],width=0.25, label='Non-Premium users',color='r')
plt.xticks(ticks=x_position,labels=grouped.index,rotation=45)
plt.title('Number of Premium and Non-Premium users by cities')
plt.ylabel('Users')
plt.legend()
plt.xlabel('Cities')
plt.show()
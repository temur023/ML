import pandas as pd
from matplotlib import pyplot as plt

orders = pd.read_csv('orders.csv')
customers = pd.read_csv('customers.csv')

# merged = orders.merge(customers,how='inner',on='customer_id')

# grouped = merged.groupby(['customer_id', 'age','is_premium'])['total_price'].sum().reset_index()

# premium = grouped[grouped['is_premium'] == True]
# non_premium = grouped[grouped['is_premium'] == False]
# plt.scatter(premium['age'], premium['total_price'], c='green',s=100,edgecolors='black',alpha=0.6,label='Premium')
# plt.scatter(non_premium['age'], non_premium['total_price'], c='blue',s=100,edgecolors='black',alpha=0.6,label='Non Premium')
# plt.legend()
# plt.xlabel('Age')
# plt.ylabel('Total Spend')
# plt.title('Age vs Spending')
# plt.show()

#Part D
plt.scatter(orders['unit_price'], orders['quantity'], c='green',s=orders['total_price']/10,edgecolors='black',alpha=0.6)
plt.xlabel('Unit Price')
plt.ylabel('Quantity')
plt.title('Unit Price vs Quantity')
plt.show()
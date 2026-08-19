from matplotlib import pyplot as plt
import pandas as pd
# #Part A
# orders = pd.read_csv('orders.csv')
# total_price = orders['total_price']
# bins = [10,30,50]
# plt.hist(total_price,bins=5,edgecolor='black',alpha=0.5)


# plt.title('Prices of Orders')
# plt.xlabel("Order Value (USD)")
# plt.ylabel("Number of Orders")

# median = total_price.median()
# plt.axvline(median, color = 'blue', linewidth=2)

#Part B
customers = pd.read_csv('customers.csv')
filtered = customers[customers['age'].notna()]

non_premium = filtered['age'][filtered['is_premium'] == False]
premium = filtered['age'][filtered['is_premium'] == True]

plt.hist(premium,bins=5,edgecolor='black',alpha=0.5,label='Premium')
plt.hist(non_premium,bins=5,edgecolor='black',alpha=0.5,label='Non Premium')

plt.title('Premium vs Non premium users')
plt.xlabel('ages')
plt.ylabel('number of users')
plt.legend()

plt.show()
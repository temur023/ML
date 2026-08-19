import pandas as pd
from matplotlib import pyplot as plt

orders = pd.read_csv('orders.csv')
customers = pd.read_csv('customers.csv')

merged = orders.merge(customers,how='inner',on='customer_id')

grouped = merged.groupby
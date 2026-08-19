import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
# print(orders.shape)
# print(orders.dtypes)
# print(orders.head())
# print(df[df["status"]=="completed"].to_string())
# print(orders[(orders["total_price"]>500) & (orders["quantity"]>=2)].to_string())

# print(customers[(customers["is_premium"] == 1) & (customers["age"] > 30)].to_string())

# print(customers.isna().sum())
# print(orders.isna().sum())

# orders = orders.fillna({"quantity":orders["quantity"].median()})

# customers = customers.dropna(subset=["age"])

# group = orders.groupby("product")
# print(group["total_price"].sum())

# group = orders.groupby("customer_id")
# print(group["total_price"].sum().sort_values(ascending=False).head(5))

# group = orders.groupby("status")
# # print(group["order_id"].count())
# # print(group["total_price"].mean())

# print(group.agg(order_count=('order_id', 'count'), avg_price=('total_price', 'mean'))) # in one call

# merged = orders.merge(customers,on="customer_id",how="inner") #JOIN
# group = merged.groupby("city")["total_price"].mean()
# print(group)

merged = customers.merge(orders,on="customer_id",how="left",indicator=True) #JOIN
never_ordered = merged[merged["_merge"] == "left_only"]
print(never_ordered[["customer_id","name","city"]])


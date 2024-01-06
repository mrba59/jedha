import pandas as pd

df_chipotle = pd.read_csv("data/chipotle.csv", index_col=0)

print(df_chipotle[['item_name', "quantity"]])
print(df_chipotle.shape)
print(df_chipotle.columns)
id_max_quantity = df_chipotle["quantity"].idxmax()
print(df_chipotle.loc[id_max_quantity, "item_name"])
print(df_chipotle.groupby("item_name")['quantity'].sum().sort_values(ascending=False))
print(df_chipotle["quantity"].sum())

df_chipotle["revenu"] = df_chipotle["item_price"].apply(lambda x: float(x[1:])) * df_chipotle["quantity"]

print(df_chipotle["revenu"].sum(axis=0))
print(df_chipotle.groupby("order_id")["revenu"].sum())

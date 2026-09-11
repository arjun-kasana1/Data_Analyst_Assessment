import pandas as pd
import numpy as np

df = pd.read_excel("Global Superstore.xls", sheet_name="Orders")

# Cleaning
text_cols = ["Ship Mode","Segment","City","State","Country","Market",
             "Region","Category","Sub-Category","Order Priority"]
for c in text_cols:
    df[c] = df[c].astype(str).str.strip()

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Quality checks
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Duplicates:", df.duplicated().sum())
print("Missing values:")
print(df.isna().sum())

df = df.drop(columns=["Postal Code"], errors="ignore")

# Feature engineering
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%b")
df["Quarter"] = "Q" + df["Order Date"].dt.quarter.astype(str)
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
df["Profit Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], 0)
df["Discount Band"] = pd.cut(
    df["Discount"],
    [-0.001, 0.10, 0.20, 0.30, 1],
    labels=["0-10%", "10-20%", "20-30%", "30%+"]
)
df["Profit Status"] = np.where(df["Profit"] < 0, "Loss", "Profit")
df["Sales per Unit"] = df["Sales"] / df["Quantity"]
df["High Sales Outlier"] = df["Sales"] > df["Sales"].quantile(0.99)
df["Discounted Sales Amount"] = df["Sales"] * df["Discount"]

# Management summaries
category = df.groupby("Category").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
category["Margin"] = category["Profit"] / category["Sales"]

market = df.groupby("Market").agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
market["Margin"] = market["Profit"] / market["Sales"]

discount = df.groupby("Discount Band", observed=False).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum"), Rows=("Profit","size")
)
discount["Margin"] = discount["Profit"] / discount["Sales"]

monthly = df.groupby(["Year","Month"]).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
).reset_index()

# Export the analysis-ready file
df.to_csv("Processed_Data.csv", index=False)
print("Processed_Data.csv created.")
print("\\nCategory summary:\\n", category)
print("\\nMarket summary:\\n", market)
print("\\nDiscount summary:\\n", discount)

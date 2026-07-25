import pandas as pd
import matplotlib.pyplot as plt


# Read CSV file
sales_data = pd.read_csv("sales_data.csv")


# Create Revenue column
sales_data["Revenue"] = sales_data["Quantity"] * sales_data["Price"]


# Total Revenue
total_revenue = sales_data["Revenue"].sum()


# Best Selling Product
best_selling = sales_data.groupby("Product")["Quantity"].sum()

best_product = best_selling.idxmax()
highest_quantity = best_selling.max()


# Highest Revenue Product
revenue_by_product = sales_data.groupby("Product")["Revenue"].sum()

highest_revenue_product = revenue_by_product.idxmax()
highest_revenue = revenue_by_product.max()


# Average Revenue
average_revenue = sales_data["Revenue"].mean()


# Top 3 Products
top_products = revenue_by_product.sort_values(
    ascending=False
).head(3)



# ==========================
# FINAL REPORT DISPLAY
# ==========================

print("=" * 50)
print("        RETAIL SALES ANALYSIS REPORT")
print("=" * 50)

print(f"Total Revenue            : ₹{total_revenue}")
print(f"Average Revenue          : ₹{average_revenue}")

print(f"\nBest Selling Product     : {best_product}")
print(f"Units Sold               : {highest_quantity}")

print(f"\nHighest Revenue Product  : {highest_revenue_product}")
print(f"Revenue Earned           : ₹{highest_revenue}")

print("\nTop 3 Products by Revenue")
print(top_products)

print("=" * 50)



# ==========================
# BAR CHART
# ==========================

plt.figure(figsize=(8,5))

revenue_by_product.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")

plt.tight_layout()

plt.show()



# ==========================
# SAVE ANALYSIS REPORT CSV
# ==========================

report = {

    "Total Revenue": [total_revenue],

    "Average Revenue": [average_revenue],

    "Best Selling Product": [best_product],

    "Units Sold": [highest_quantity],

    "Highest Revenue Product": [highest_revenue_product],

    "Highest Revenue": [highest_revenue]

}


report_df = pd.DataFrame(report)


report_df.to_csv(
    "sales_analysis_report.csv",
    index=False
)


print("Report saved successfully!")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Page title
st.title("Retail Sales Data Analyzer 📊")


# Read CSV file
data = pd.read_csv("sales_data.csv")


# Create Revenue column
data["Revenue"] = data["Quantity"] * data["Price"]


# Show sales data
st.subheader("Sales Data")
st.dataframe(data)


# ---------------------------
# Sales Insights
# ---------------------------

st.subheader("Sales Insights")


# Total Revenue
total_revenue = data["Revenue"].sum()

st.metric(
    "Total Revenue",
    f"₹ {total_revenue}"
)


# Average Revenue
average_revenue = data["Revenue"].mean()

st.metric(
    "Average Revenue Per Sale",
    f"₹ {average_revenue:.2f}"
)


# Best Selling Product
best_product = (
    data.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

units_sold = (
    data.groupby("Product")["Quantity"]
    .sum()
    .max()
)


st.write(
    "🏆 Best Selling Product:",
    best_product
)

st.write(
    "Units Sold:",
    units_sold
)



# Highest Revenue Product

revenue_product = (
    data.groupby("Product")["Revenue"]
    .sum()
)

highest_product = revenue_product.idxmax()

highest_revenue = revenue_product.max()


st.write(
    "💰 Highest Revenue Product:",
    highest_product
)

st.write(
    "Revenue Earned:",
    f"₹ {highest_revenue}"
)



# ---------------------------
# Chart
# ---------------------------

st.subheader("Revenue by Product")


fig, ax = plt.subplots()

revenue_product.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Product")
ax.set_ylabel("Revenue (₹)")
ax.set_title("Revenue Analysis")


st.pyplot(fig)
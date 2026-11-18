
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from database import get_connection

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"
CHART_DIR = REPORT_DIR / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")


def load_sales_data():

    connection = get_connection()

    query = """
        SELECT
            o.order_id,
            o.order_date,
            c.customer_name,
            c.region,
            p.product_name,
            p.category,
            s.quantity,
            s.unit_price,
            s.cost_price,
            s.revenue,
            s.profit
        FROM sales s
        JOIN orders o
            ON s.order_id = o.order_id
        JOIN customers c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON s.product_id = p.product_id
        ORDER BY o.order_date;
    """

    try:
        df = pd.read_sql_query(query, connection)
        print("Sales data loaded successfully!")
        return df

    finally:
        connection.close()


def perform_analysis(df):

    print("\n========== SALES ANALYSIS ==========")

    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_name"].nunique()
    total_quantity = df["quantity"].sum()

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue else 0
    )

    print(f"Total Revenue: Rs. {total_revenue:,.2f}")
    print(f"Total Profit: Rs. {total_profit:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Total Customers: {total_customers}")
    print(f"Total Products Sold: {total_quantity}")
    print(f"Profit Margin: {profit_margin:.2f}%")

    # Product analysis
    product_sales = (
        df.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== TOP PRODUCTS ==========")
    print(product_sales.head(5))

    # Regional analysis
    region_sales = (
        df.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== REGIONAL SALES ==========")
    print(region_sales)

    # Category analysis
    category_sales = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== CATEGORY SALES ==========")
    print(category_sales)

    # Monthly analysis
    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly_sales = (
        df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
        .sum()
    )

    print("\n========== MONTHLY SALES ==========")
    print(monthly_sales)

    # Save summary report
    with open(REPORT_DIR / "business_insights.txt", "w") as file:

        file.write("SALES BUSINESS ANALYSIS REPORT\n")
        file.write("==============================\n\n")

        file.write(f"Total Revenue: Rs. {total_revenue:,.2f}\n")
        file.write(f"Total Profit: Rs. {total_profit:,.2f}\n")
        file.write(f"Total Orders: {total_orders}\n")
        file.write(f"Total Customers: {total_customers}\n")
        file.write(f"Total Quantity Sold: {total_quantity}\n")
        file.write(f"Profit Margin: {profit_margin:.2f}%\n\n")

        file.write("Top Products:\n")
        file.write(product_sales.to_string())

        file.write("\n\nRegional Sales:\n")
        file.write(region_sales.to_string())

        file.write("\n\nCategory Sales:\n")
        file.write(category_sales.to_string())

        file.write("\n\nMonthly Sales:\n")
        file.write(monthly_sales.to_string())

    print("\nBusiness insights report saved!")


def create_visualizations(df):

    print("\nCreating sales charts...")

    # 1. Monthly revenue trend
    monthly = (
        df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
        .sum()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(monthly.index.astype(str), monthly.values, marker="o")
    plt.title("Monthly Sales Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_sales.png")
    plt.close()

    # 2. Top products
    products = (
        df.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 5))
    plt.bar(products.index, products.values)
    plt.title("Product-wise Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "product_sales.png")
    plt.close()

    # 3. Regional sales
    regions = df.groupby("region")["revenue"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(regions.index, regions.values)
    plt.title("Regional Sales Performance")
    plt.xlabel("Region")
    plt.ylabel("Revenue (Rs.)")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "regional_sales.png")
    plt.close()

    # 4. Category revenue
    categories = df.groupby("category")["revenue"].sum()

    plt.figure(figsize=(7, 7))
    plt.pie(
        categories.values,
        labels=categories.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Category-wise Revenue Distribution")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "category_sales.png")
    plt.close()

    # 5. Profit analysis
    profit = df.groupby("category")["profit"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(profit.index, profit.values)
    plt.title("Category-wise Profit")
    plt.xlabel("Category")
    plt.ylabel("Profit (Rs.)")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "category_profit.png")
    plt.close()

    print("All five charts created successfully!")


if __name__ == "__main__":

    sales_df = load_sales_data()

    if sales_df.empty:
        print("No sales records found.")
    else:
        perform_analysis(sales_df)
        create_visualizations(sales_df)


import pandas as pd
from pathlib import Path


def clean_sales_data():

    file_path = (
        Path(__file__).resolve().parent.parent
        / "dataset"
        / "sales_data.csv"
    )

    print("Reading sales dataset...")

    df = pd.read_csv(file_path)

    # Remove duplicate orders
    df = df.drop_duplicates(subset=["order_id"])

    # Remove rows with missing required values
    required_columns = [
        "order_id", "order_date", "customer_name",
        "product_name", "category", "region",
        "quantity", "unit_price", "cost_price"
    ]

    df = df.dropna(subset=required_columns)

    # Convert data types
    df["order_id"] = pd.to_numeric(
        df["order_id"], errors="raise"
    ).astype(int)

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="raise"
    )

    numeric_columns = [
        "quantity", "unit_price", "cost_price"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="raise"
        )

    # Validate values
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    if (df[["unit_price", "cost_price"]] < 0).any().any():
        raise ValueError("Prices cannot be negative.")

    # Remove unnecessary spaces
    for column in [
        "customer_name", "product_name", "category", "region"
    ]:
        df[column] = df[column].astype(str).str.strip()

    if (df[["customer_name", "product_name", "category", "region"]] == "").any().any():
        raise ValueError("Text fields cannot be empty.")

    print("Data cleaning completed!")
    print("Total valid records:", len(df))

    return df

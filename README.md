# Sales Data Analysis & Business Intelligence Dashboard

An end-to-end data analytics project that uses Python, PostgreSQL, SQL, and Microsoft Power BI to analyze sales performance and generate business insights through an interactive dashboard.

## Project Overview

This project analyzes sales data to understand business performance, identify top-performing products, evaluate regional sales, and track revenue and profit trends.

The project includes data cleaning, database management, SQL analysis, exploratory data analysis (EDA), and an interactive Power BI dashboard.

## Project Objectives

- Analyze overall sales revenue and profitability.
- Identify the top-performing products.
- Compare sales performance across regions.
- Analyze revenue by product category.
- Track monthly revenue trends.
- Build an interactive business intelligence dashboard.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| PostgreSQL | Database storage |
| SQL | Data querying and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Power BI | Interactive dashboard |
| VS Code | Development environment |

## Project Structure

```text
Sales-Data-Analysis/
│
├── dataset/
│   └── sales_data.csv
│
├── powerbi/
│   └── Sales_Performance_Dashboard.pbix
│
├── python/
│   ├── database.py
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   └── main.py
│
├── reports/
│   ├── business_insights.txt
│   └── charts/
│       ├── category_profit.png
│       ├── category_sales.png
│       ├── monthly_sales.png
│       ├── product_sales.png
│       └── regional_sales.png
│
├── sql/
│   ├── create_tables.sql
│   └── sales_queries.sql
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Project Workflow

1. **Data Collection:** Loaded sales records from a CSV dataset.
2. **Data Cleaning:** Used Python and Pandas to clean and prepare the data.
3. **Database Management:** Created relational tables in PostgreSQL.
4. **Data Integration:** Imported customer, product, order, and sales records into the database.
5. **SQL Analysis:** Executed SQL queries to calculate revenue, profit, regional performance, and product performance.
6. **Exploratory Data Analysis:** Used Python to analyze sales trends and generate charts.
7. **Business Intelligence:** Developed an interactive Power BI dashboard.

## Key Business Insights

Based on the sample dataset:

| Business Metric | Result |
|---|---:|
| Total Revenue | ₹476,500 |
| Total Profit | ₹130,000 |
| Total Orders | 15 |
| Total Customers | 15 |
| Quantity Sold | 45 |
| Profit Margin | 27.28% |

### Monthly Revenue

| Month | Revenue |
|---|---:|
| January 2026 | ₹218,500 |
| February 2026 | ₹35,000 |
| March 2026 | ₹53,000 |
| April 2026 | ₹51,000 |
| May 2026 | ₹119,000 |

### Additional Findings

- **Top Product:** Laptop – ₹165,000 revenue.
- **Top Region:** South – ₹177,000 revenue.
- **Top Category:** Electronics – ₹365,000 revenue.
- The Electronics category generated more revenue than Furniture in this dataset.

## Power BI Dashboard

The interactive dashboard includes:

- Total Revenue KPI.
- Total Profit KPI.
- Total Orders KPI.
- Total Customers KPI.
- Profit Margin KPI.
- Monthly Revenue Analysis.
- Region-wise Sales Analysis.
- Category-wise Sales Analysis.
- Top 5 Products by Revenue.

### Interactive Filters

Users can filter dashboard results using:

- Region slicer.
- Product Category slicer.
- Order Date slicer.

## SQL Analysis

The SQL analysis includes queries for:

- Overall business performance.
- Top-selling products.
- Regional revenue analysis.
- Category-wise sales.
- Monthly revenue and profit.
- Top customers.
- Month-over-month revenue growth.
- Product profitability.
- Daily sales analysis.
- Profit margin calculation.

SQL scripts are available in the `sql/` folder.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Sales-Data-Analysis.git
cd Sales-Data-Analysis
```

Replace `saitejaengili` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named:

```text
sales_analysis_db
```

Execute `sql/create_tables.sql` in pgAdmin Query Tool to create the required tables.

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sales_analysis_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

Use your own PostgreSQL credentials. Never upload the `.env` file to GitHub.

### 5. Run the Python Project

Clean the dataset:

```bash
python .\python\data_cleaning.py
```

Import the sales data:

```bash
python .\python\main.py
```

Run data analysis:

```bash
python .\python\data_analysis.py
```

### 6. Open the Power BI Dashboard

Open:

```text
powerbi/Sales_Performance_Dashboard.pbix
```

Use Power BI Desktop to explore the interactive dashboard.

## Dataset Information

The project uses a sample sales dataset containing 15 sales records from January to May 2026.

The dataset includes:

- Order ID
- Order Date
- Customer Name
- Product Name
- Category
- Region
- Quantity
- Unit Price
- Cost Price

The reported metrics and insights are based on this sample dataset.

## Future Improvements

- Analyze larger real-world sales datasets.
- Build automated data refresh pipelines.
- Add sales forecasting.
- Develop advanced customer segmentation.
- Integrate machine learning for sales prediction.

## Author

**Sai Teja**

Computer Science Student | Data Analysis Enthusiast

**Project:** Sales Data Analysis and Business Intelligence Dashboard

**Technologies:** Python | PostgreSQL | SQL | Power BI

---

If you find this project useful, feel free to explore the repository and its implementation.
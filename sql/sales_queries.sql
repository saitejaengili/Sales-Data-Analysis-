
-- ==========================================
-- SALES BUSINESS INTELLIGENCE ANALYSIS
-- ==========================================

-- 1. Overall Business Performance
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_quantity_sold,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    ROUND(
        SUM(profit) / NULLIF(SUM(revenue), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM sales;


-- 2. Top 5 Revenue Generating Products
SELECT
    p.product_name,
    p.category,
    SUM(s.quantity) AS total_quantity,
    SUM(s.revenue) AS total_revenue,
    SUM(s.profit) AS total_profit
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 5;


-- 3. Region-wise Sales Performance
SELECT
    c.region,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(s.revenue) AS total_revenue,
    SUM(s.profit) AS total_profit
FROM sales s
JOIN orders o
    ON s.order_id = o.order_id
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;


-- 4. Category-wise Sales Analysis
SELECT
    p.category,
    SUM(s.quantity) AS total_quantity,
    SUM(s.revenue) AS total_revenue,
    SUM(s.profit) AS total_profit
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;


-- 5. Monthly Revenue and Profit
SELECT
    TO_CHAR(o.order_date, 'YYYY-MM') AS sales_month,
    SUM(s.revenue) AS monthly_revenue,
    SUM(s.profit) AS monthly_profit
FROM sales s
JOIN orders o
    ON s.order_id = o.order_id
GROUP BY DATE_TRUNC('month', o.order_date),
         TO_CHAR(o.order_date, 'YYYY-MM')
ORDER BY DATE_TRUNC('month', o.order_date);


-- 6. Top 5 Customers
SELECT
    c.customer_name,
    c.region,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(s.revenue) AS total_purchase
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN sales s
    ON o.order_id = s.order_id
GROUP BY c.customer_id, c.customer_name, c.region
ORDER BY total_purchase DESC
LIMIT 5;


-- 7. Monthly Revenue Growth Percentage
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(s.revenue) AS revenue
    FROM sales s
    JOIN orders o
        ON s.order_id = o.order_id
    GROUP BY DATE_TRUNC('month', o.order_date)
),
growth AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS previous_revenue
    FROM monthly_sales
)
SELECT
    TO_CHAR(month, 'YYYY-MM') AS sales_month,
    revenue,
    previous_revenue,
    ROUND(
        (revenue - previous_revenue)
        / NULLIF(previous_revenue, 0) * 100,
        2
    ) AS growth_percentage
FROM growth
ORDER BY month;


-- 8. Most Profitable Products
SELECT
    p.product_name,
    SUM(s.profit) AS total_profit
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_profit DESC;


-- 9. Daily Sales Performance
SELECT
    o.order_date,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(s.revenue) AS daily_revenue,
    SUM(s.profit) AS daily_profit
FROM orders o
JOIN sales s
    ON o.order_id = s.order_id
GROUP BY o.order_date
ORDER BY o.order_date;


-- 10. Product Profit Margin
SELECT
    p.product_name,
    SUM(s.revenue) AS total_revenue,
    SUM(s.profit) AS total_profit,
    ROUND(
        SUM(s.profit) / NULLIF(SUM(s.revenue), 0) * 100,
        2
    ) AS profit_margin
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY profit_margin DESC;

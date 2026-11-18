
-- ==========================================
-- SALES DATA ANALYSIS PROJECT
-- Database: sales_analysis_db
-- ==========================================

-- 1. CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL UNIQUE,
    region VARCHAR(50) NOT NULL
);

-- 2. PRODUCTS TABLE
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
    cost_price NUMERIC(12,2) NOT NULL CHECK (cost_price >= 0)
);

-- 3. ORDERS TABLE
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- 4. SALES TABLE
CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12,2) NOT NULL,
    cost_price NUMERIC(12,2) NOT NULL,

    revenue NUMERIC(14,2)
        GENERATED ALWAYS AS (quantity * unit_price) STORED,

    profit NUMERIC(14,2)
        GENERATED ALWAYS AS
        (quantity * (unit_price - cost_price)) STORED,

    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT unique_order_product
        UNIQUE (order_id, product_id),

    CHECK (unit_price >= 0),
    CHECK (cost_price >= 0)
);

-- 5. CREATE INDEXES
CREATE INDEX IF NOT EXISTS idx_orders_date
ON orders(order_date);

CREATE INDEX IF NOT EXISTS idx_sales_product
ON sales(product_id);

CREATE INDEX IF NOT EXISTS idx_orders_customer
ON orders(customer_id);

-- SUCCESS MESSAGE
SELECT 'Sales database tables created successfully!' AS status;

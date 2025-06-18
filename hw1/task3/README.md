# SQL Queries for Orders Table Analysis

This file contains SQL queries to analyze the `orders` table and perform various business intelligence tasks.

## Table Structure

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);
```

## Query Tasks

### Task 1: Calculate Total Sales Volume for March 2024

**Primary Query:**
```sql
SELECT 
    SUM(amount) AS total_sales_march_2024
FROM orders 
WHERE strftime('%Y-%m', order_date) = '2024-03';
```

**Alternative (Date Range):**
```sql
SELECT 
    SUM(amount) AS total_sales_march_2024
FROM orders 
WHERE order_date >= '2024-03-01' 
  AND order_date < '2024-04-01';
```

**Explanation:**
- Uses SQLite's `strftime()` function to extract year-month from the date
- Filters for March 2024 specifically
- Alternative approach uses explicit date range for clarity

### Task 2: Find Customer with Highest Total Spending

**Primary Query:**
```sql
SELECT 
    customer,
    SUM(amount) AS total_spent
FROM orders 
GROUP BY customer 
ORDER BY total_spent DESC 
LIMIT 1;
```

**Alternative (Ranked List):**
```sql
SELECT 
    customer,
    SUM(amount) AS total_spent,
    RANK() OVER (ORDER BY SUM(amount) DESC) AS spending_rank
FROM orders 
GROUP BY customer;
```

**Explanation:**
- Groups orders by customer and calculates total spending per customer
- Orders by total spending in descending order
- `LIMIT 1` returns only the top spender
- Alternative shows all customers ranked by spending

### Task 3: Calculate Average Order Value for Last 3 Months

**Primary Query:**
```sql
SELECT 
    AVG(amount) AS avg_order_value_last_3_months
FROM orders 
WHERE order_date >= date('now', '-3 months')
  AND order_date <= date('now');
```

**Detailed Breakdown:**
```sql
SELECT 
    strftime('%Y-%m', order_date) AS month,
    COUNT(*) AS order_count,
    AVG(amount) AS avg_order_value,
    SUM(amount) AS total_sales
FROM orders 
WHERE order_date >= date('now', '-3 months')
  AND order_date <= date('now')
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;
```

**Explanation:**
- Uses SQLite's `date('now', '-3 months')` to get date 3 months ago
- Filters orders from 3 months ago to current date
- Calculates average order value for this period
- Detailed version shows breakdown by month

## Comprehensive Query

The file also includes a comprehensive query using Common Table Expressions (CTEs) that combines all three tasks into a single result set.

## SQLite-Specific Features Used

1. **`strftime()`**: Date formatting function for extracting year-month
2. **`date()`**: Date manipulation functions
3. **`RANK() OVER()`**: Window function for ranking (SQLite 3.25+)
4. **Common Table Expressions (CTEs)**: For complex query organization

## Usage

1. Ensure you have SQLite installed
2. Create the orders table with the provided schema
3. Insert sample data
4. Run the desired queries from `sql_queries.sql`

## Sample Data Insertion

```sql
INSERT INTO orders (customer, amount, order_date) VALUES
('John Doe', 150.00, '2024-03-15'),
('Jane Smith', 200.00, '2024-03-20'),
('John Doe', 75.50, '2024-02-10'),
('Bob Johnson', 300.00, '2024-01-05'),
('Jane Smith', 125.00, '2024-02-28');
``` 
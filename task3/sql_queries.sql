-- SQL Queries for Orders Table Analysis
-- Table Structure:
-- CREATE TABLE orders (
--     id INTEGER PRIMARY KEY,
--     customer TEXT,
--     amount REAL,
--     order_date DATE
-- );

-- Task 1: Calculate the total sales volume for March 2024
SELECT 
    SUM(amount) AS total_sales_march_2024
FROM orders 
WHERE strftime('%Y-%m', order_date) = '2024-03';

-- Alternative approach using date range (more explicit)
SELECT 
    SUM(amount) AS total_sales_march_2024
FROM orders 
WHERE order_date >= '2024-03-01' 
  AND order_date < '2024-04-01';

-- Task 2: Find the customer who spent the most overall (highest total amount across all orders)
SELECT 
    customer,
    SUM(amount) AS total_spent
FROM orders 
GROUP BY customer 
ORDER BY total_spent DESC 
LIMIT 1;

-- Alternative approach to get all customers ranked by spending
SELECT 
    customer,
    SUM(amount) AS total_spent,
    RANK() OVER (ORDER BY SUM(amount) DESC) AS spending_rank
FROM orders 
GROUP BY customer;

-- Task 3: Calculate the average order value for the last three months relative to the current date
SELECT 
    AVG(amount) AS avg_order_value_last_3_months
FROM orders 
WHERE order_date >= date('now', '-3 months')
  AND order_date <= date('now');

-- Alternative approach with more detailed breakdown
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

-- Comprehensive query combining all three tasks
WITH monthly_sales AS (
    SELECT 
        strftime('%Y-%m', order_date) AS month,
        SUM(amount) AS total_sales
    FROM orders 
    WHERE strftime('%Y-%m', order_date) = '2024-03'
),
top_customer AS (
    SELECT 
        customer,
        SUM(amount) AS total_spent
    FROM orders 
    GROUP BY customer 
    ORDER BY total_spent DESC 
    LIMIT 1
),
recent_avg AS (
    SELECT 
        AVG(amount) AS avg_order_value
    FROM orders 
    WHERE order_date >= date('now', '-3 months')
      AND order_date <= date('now')
)
SELECT 
    (SELECT total_sales FROM monthly_sales) AS march_2024_sales,
    (SELECT customer FROM top_customer) AS top_spending_customer,
    (SELECT total_spent FROM top_customer) AS top_customer_total_spent,
    (SELECT avg_order_value FROM recent_avg) AS last_3_months_avg_order_value; 
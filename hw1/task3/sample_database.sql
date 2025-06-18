-- Sample Database for Orders Table Analysis
-- This file creates the table and inserts sample data for testing the queries

-- Create the orders table
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);

-- Insert sample data
INSERT INTO orders (customer, amount, order_date) VALUES
(1, 'John Doe', 150.00, '2024-03-15'),
(2, 'Jane Smith', 200.00, '2024-03-20'),
(3, 'John Doe', 75.50, '2024-02-10'),
(4, 'Bob Johnson', 300.00, '2024-01-05'),
(5, 'Jane Smith', 125.00, '2024-02-28'),
(6, 'Alice Brown', 180.00, '2024-03-10'),
(7, 'Charlie Wilson', 95.00, '2024-03-25'),
(8, 'John Doe', 220.00, '2024-01-20'),
(9, 'Diana Davis', 160.00, '2024-02-15'),
(10, 'Bob Johnson', 140.00, '2024-03-05'),
(11, 'Jane Smith', 90.00, '2024-01-30'),
(12, 'Alice Brown', 110.00, '2024-02-20'),
(13, 'Charlie Wilson', 175.00, '2024-03-12'),
(14, 'Diana Davis', 85.00, '2024-01-15'),
(15, 'John Doe', 195.00, '2024-02-25');

-- Verify the data
SELECT 'Total orders:' AS info, COUNT(*) AS count FROM orders
UNION ALL
SELECT 'Unique customers:', COUNT(DISTINCT customer) FROM orders
UNION ALL
SELECT 'Date range:', MIN(order_date) || ' to ' || MAX(order_date) FROM orders; 
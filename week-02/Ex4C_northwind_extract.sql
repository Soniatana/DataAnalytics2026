-- Ex4C Northwind Extract

-- The table that holds the categories of items Northwind sells is the Categories table.
-- The table that holds the items Northwind sells is the Products table.

SELECT * FROM northwind.employees;
-- The employee whose name looks like a bird is Nancy Davolio.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM northwind.orders
LIMIT 50;


SELECT * FROM northwind.products;
-- This query returns 77 records.
-- You can change the number of rows returned by adjusting the limit option in MySQL Workbench to 10

-- BONUS: Limit rows using SQL
SELECT * FROM northwind.products LIMIT 10;
-- This query limits the output to only 10 rows using the LIMIT clause.

SELECT * FROM northwind.categories;
-- The CategoryID of Seafood is 8.
-- Q8: Orders Table (Top 50 Records)

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM northwind.orders
LIMIT 50;
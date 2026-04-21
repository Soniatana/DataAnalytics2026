USE northwind;
-- Q1: List product id, name, and unit price
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- Q2: Products with unit price 7.50 or less
SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.50;

-- Q3: No units in stock but on backorder
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0
AND UnitsOnOrder >= 1;

-- View categories
SELECT * FROM Categories;

-- Seafood products
SELECT p.ProductName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

-- Find supplier ID for Tokyo Traders
SELECT ProductID, ProductName, UnitPrice
FROM Products;
SELECT * FROM Suppliers;
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- Employees with 'manager' in title
SELECT FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%manager%';



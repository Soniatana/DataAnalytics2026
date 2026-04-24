USE northwind;
SELECT MIN(UnitPrice) AS CheapestPrice
FROM Products;

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice = (
    SELECT MIN(UnitPrice) FROM Products
);

Q2 Average price
SELECT AVG(UnitPrice) AS AveragePrice
FROM Products;

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;

Q3 Most expensive product + supplier 
SELECT MAX(UnitPrice) AS HighestPrice
FROM Products;

SELECT MAX(UnitPrice) AS HighestPrice
FROM Products;

SELECT p.ProductName, p.UnitPrice, s.CompanyName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice) FROM Products
);

Q4 Total payroll
SELECT SUM(Salary) AS TotalPayroll
FROM Employees;

Q5 highest lowest salary
SELECT 
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;

Q6 supplier + number of products
SELECT 
    s.SupplierID,
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfProducts
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

Q7 Category + Average price
SELECT 
    c.CategoryName,
    AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

Q8 Suppliers with atleast 5 products
SELECT 
    s.CompanyName,
    COUNT(p.ProductID) AS NumberOfProducts
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

Q9 Inventory value
SELECT 
    ProductID,
    ProductName,
    UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;

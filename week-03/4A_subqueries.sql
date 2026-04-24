USE northwind;

-- Q1 Most expensive product(s)
SELECT ProductName
FROM Products
WHERE UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM Products
    );
    
  -- Q2 Least expensive product(s) and category
  SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM Products
);

-- Q3 Orders shipped via Federal Shipping
SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = (
    SELECT ShipperID
    FROM Shippers
    WHERE CompanyName = 'Federal Shipping'
);

-- Q4 Orders containing Sasquatch Ale
SELECT OrderID
FROM `Order Details`
WHERE ProductID = (
    SELECT ProductID
    FROM Products
    WHERE ProductName = 'Sasquatch Ale'
);

-- Q5 Employee for order 10266
SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = (
    SELECT EmployeeID
    FROM Orders
    WHERE OrderID = 10266
);

-- Q6 Customer for order 10266
SELECT CompanyName
FROM Customers
WHERE CustomerID = (
    SELECT CustomerID
    FROM Orders
    WHERE OrderID = 10266
);


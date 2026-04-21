USE northwind;

-- Q1
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName
FROM Products p
JOIN Categories c
    ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- Q2
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    s.CompanyName
FROM Products p
JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName;

-- Q3
SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName
FROM Products p
JOIN Categories c
    ON p.CategoryID = c.CategoryID
JOIN Suppliers s
    ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

-- Q4
SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    s.CompanyName AS Shipper
FROM Orders o
JOIN Shippers s
    ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY s.CompanyName, o.ShipName;

-- Q5
SELECT 
    o.ShipName,
    COUNT(*) AS OrderCount
FROM Orders o
JOIN Shippers s
    ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName
ORDER BY OrderCount DESC;

-- Q6
SELECT 
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM Orders o
JOIN `Order Details` od
    ON o.OrderID = od.OrderID
JOIN Products p
    ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';
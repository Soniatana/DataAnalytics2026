-- Q1: Products sorted by price (ascending)
SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC;

-- Q2: At least 100 units in stock (highest price first)
SELECT ProductName, UnitsInStock, UnitPrice
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- Q3: Same as Q2 + tie-break by name

SELECT ProductName, UnitsInStock, UnitPrice
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- Q4: Count distinct customers
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;

-- Q5: Distinct customers per country
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- Q6: Low stock but on order
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- Q7: Count employees per job title
SELECT Title, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;

-- Q8: Employees with salary between 2000 and 2500
SELECT FirstName, LastName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;
SELECT * FROM Employees;


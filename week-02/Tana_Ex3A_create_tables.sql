DROP SCHEMA IF EXISTS lANA_dog_walking;
CREATE SCHEMA lana_dog_walking;
USE lana_dog_walking;
CREATE TABLE Customers (
CustomerID INT PRIMARY KEY,
Name VARCHAR(100),
Phone VARCHAR(20),
Address VARCHAR(255),
Email VARCHAR(100)
);
CREATE TABLE Dogs (
DogID INT PRIMARY KEY,
Name VARCHAR(100),
Breed VARCHAR(100),
AGE INT,
CustomerID INT,
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
CREATE TABLE Walks (
WalkId INT PRIMARY KEY,
Date DATE,
Time TIME,
Duration INT,
DogID INT,
FOREIGN KEY (DogID) REFERENCES Dogs(DogID)
);
CREATE TABLE payments (
paymentID INT PRIMARY KEY,
Amount DECIMAL(5,2),
Date DATE,
CustomerID INT,
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

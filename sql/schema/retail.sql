
CREATE TABLE retail_data (
    Category TEXT,
    Sub_Category TEXT,
    Sales REAL,
    Profit REAL
);

INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Furniture', 'Chairs', 500.00, 50.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Furniture', 'Chairs', 300.00, 30.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Furniture', 'Tables', 400.00, -20.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Technology', 'Phones', 1000.00, 200.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Technology', 'Phones', 1200.00, 240.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Technology', 'Accessories', 150.00, 15.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Office Supplies', 'Binders', 250.00, 25.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Office Supplies', 'Binders', 300.00, 18.00);
INSERT INTO retail_data(Category, Sub_Category, Sales, Profit) VALUES ('Office Supplies', 'Paper', 100.00, 5.00);

SELECT 
    Category,
    Sub_Category,
    SUM(Sales) AS Subcategory_Sales,
    SUM(Profit) AS Subcategory_Profit,
    ROUND(SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0), 2) AS Subcategory_Profit_Margin_Percent
FROM 
    retail_data
GROUP BY 
    Category, Sub_Category
ORDER BY 
    Category, Sub_Category;

SELECT 
    Category,
    SUM(Sales) AS Category_Sales,
    SUM(Profit) AS Category_Profit,
    ROUND(SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0), 2) AS Category_Profit_Margin_Percent
FROM 
    retail_data
GROUP BY 
    Category
ORDER BY 
    Category;

SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0), 2) AS Overall_Profit_Margin_Percent
FROM 
    retail_data;

# 📊 Retail Analysis Project

A cross-functional data analytics dashboard developed using **Python**, **JavaScript**, **SQL**, and **Power BI**, designed to evaluate retail metrics like customer trends, spending behavior, and profit margins across global segments and product categories.

---

## 📁 Project Structure

├── Gyanankur_Retail.csv ├── README.md ├── Retail Profit Margin Analyzer │   ├── calculateProfitMargin.js │   ├── profit_summary.csv ├── power bi │   ├── IMG20250623232940-Picsart-AiImageEnhancer.jpg ├── python │   ├── Retail_Analysis.py │   ├── outputs │   │   ├── IMG20250623065733.jpg │   │   ├── IMG20250623065749.jpg │   │   ├── IMG20250623065809.jpg │   │   ├── IMG20250623065837.jpg │   │   ├── IMG20250623065912.jpg │   │   ├── IMG20250623065928.jpg │   │   ├── IMG20250623065949.jpg ├── reports │   ├── Retail Data Visualization.pdf │   ├── Retail Insights Dashboard.pdf ├── sql │   ├── output │   │   ├── IMG20250622230727.png │   │   ├── retail_output.md │   ├── schema │   │   ├── IMG20250622230709.png │   │   ├── retail.sql │   ├── tables │   │   ├── IMG20250622230744.png │   │   ├── show_tables.sql

---

## ✨ Key Features

- 📈 Interactive Dash App with Plotly & Dash
- 🧮 JavaScript-based category-level profit margin computation
- 💾 SQL queries for category, subcategory, and overall profit metrics
- 📊 Power BI dashboards and Python-generated visuals
- 📂 Organized structure for scalable exploration

---

## 🐍 Python: Data Processing & Dash App

```python
df = pd.read_csv('Gyanankur_Retail.csv')
df['Age Group'] = pd.cut(df['Age'], bins=[0, 20, 30, 45, 60, 100],
                         labels=['Teen', 'Young Adult', 'Adult', 'Senior', 'Elder'])

fig_map = px.choropleth(sales_by_country, locations='Country', color='TotalAmount')

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2('Retail Analytics Dashboard'),
    dcc.Graph(figure=fig_map),
    html.Img(src='violinsegmentgender.png', style={'width': '60%'})
])

```
---

🧮 JavaScript: Profit Margin Calculator

```javascript

const categoryMargins = {};
// Reading CSV and calculating average margins

fs.createReadStream('Gyanankur_Retail.csv')
  .pipe(csv())
  .on('data', (row) => {
    const cost = parseFloat(row.Amount);
    const revenue = parseFloat(row.Total_Amount);
    const key = `${row.ProductCategory || 'Unknown'} > ${row.ProductType || 'Unknown'}`;
    // ... margin logic
  })
  .on('end', () => {
    fs.writeFile('profit_summary.csv', ...);
    console.table(summary);
  });

```
🔍 Sample Output (from profit_summary.csv)

```csv
CategorySubcategory	AvgProfit_Margin	Entries

Clothing > Shorts	69.96%	505
Electronics > Tablet	68.88%	1041
Home Decor > Tools	71.51%	491
Grocery > Juice	69.23%	1014
Unknown Category > Jacket	90.00%	1

```

---

📂 SQL: Profit Margin Queries

```sql

SELECT 
    Category,
    SUM(Sales) AS Category_Sales,
    SUM(Profit) AS Category_Profit,
    ROUND(SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0), 2) AS CategoryProfitMargin_Percent
FROM 
    retail_data
GROUP BY 
    Category
ORDER BY 
    Category;

```
---

📸 Visual Gallery

🧭 Power BI Dashboard



📈 Python Visuals

      

🧬 SQL Schema & Output

Schema View



Query Output



Table Structure




---

📘 Reports & Dashboards

📘 Retail Data Visualization (PDF)

📗 Retail Insights Dashboard (PDF)



---

Here's a clear and organized list of output images and files that are visually shown (or meant to be shown) in your README.md, broken down snippet-wise by language:


---

🐍 Python: Output List from Retail_Analysis.py

Markdown Code Snippet Block:

df = pd.read_csv('Gyanankur_Retail.csv')
...
app = dash.Dash(__name__)

Output Images Rendered After Python Snippet:

Index	File Path	Description

1️⃣	python/outputs/IMG20250623065733.jpg	Choropleth Map / Visual 1
2️⃣	python/outputs/IMG20250623065749.jpg	Visual 2 (possibly age group distribution)
3️⃣	python/outputs/IMG20250623065809.jpg	Visual 3
4️⃣	python/outputs/IMG20250623065837.jpg	Visual 4
5️⃣	python/outputs/IMG20250623065912.jpg	Visual 5
6️⃣	python/outputs/IMG20250623065928.jpg	Visual 6
7️⃣	python/outputs/IMG20250623065949.jpg	Visual 7



---

🧮 JavaScript: Output from calculateProfitMargin.js

Markdown Code Snippet Block:

fs.createReadStream('Gyanankur_Retail.csv')
  .pipe(csv())
  ...
  .on('end', () => {
    fs.writeFile('profit_summary.csv', ...);
  });

Output Table Rendered in Markdown:

CategorySubcategory	AvgProfit_Margin	Entries

Clothing > Shorts	69.96%	505
Electronics > Tablet	68.88%	1041
Home Decor > Tools	71.51%	491
Grocery > Juice	69.23%	1014
Unknown Category > Jacket	90.00%	1


Output File (not an image, but mentioned):

📄 Retail Profit Margin Analyzer/profit_summary.csv



---

📂 SQL: Output from Queries in retail.sql

Markdown Code Snippet Block:

SELECT 
    Category,
    SUM(Sales) AS Category_Sales,
    ...

Output Images Rendered After SQL Snippet:

Index	File Path	Description

🧬	sql/schema/IMG20250622230709.png	Database Schema View
📊	sql/output/IMG20250622230727.png	SQL Query Result
📋	sql/tables/IMG20250622230744.png	Table Structure View



---

📊 Power BI Dashboard

Markdown Section:

### 🧭 Power BI Dashboard

Output Image:

File Path	Description

power bi/IMG20250623232940-Picsart-AiImageEnhancer.jpg	Final Power BI Dashboard Visual



---

📘 PDF Reports (Linked)

File Path	Document Title

reports/Retail Data Visualization.pdf	📘 Retail Data Visualization
reports/Retail Insights Dashboard.pdf	📗 Retail Insights Dashboard



---

Would you like me to generate a collapsible Table of Contents or auto-thumbnail version too?



👤 Author & License

GitHub: @Gyanankur23
License: MIT License


---

🔖 Hashtags (Markdown Friendly)

#RetailAnalytics #PowerBI #DataScience #PythonDash #SQLAnalytics #ProfitMargin #BusinessIntelligence #JS #EDA #RetailDashboard #CustomerSegmentation #GyanankurBaruah

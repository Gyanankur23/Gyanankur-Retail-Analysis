import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import dash
from dash import dcc, html
import warnings
warnings.filterwarnings('ignore')

# Load and clean data
df = pd.read_csv('Gyanankur_Retail.csv')
df.columns = df.columns.str.strip()

expected_cols = ['Date', 'Time', 'Age', 'Gender', 'Customer_Segment', 'Income', 'Order_Status',
                 'Payment_Method', 'Ratings', 'Total_Amount', 'Total_Purchases', 'Country',
                 'Product_Category', 'Product_Brand']
missing = [col for col in expected_cols if col not in df.columns]
if missing:
    raise KeyError(f"Missing expected column(s): {missing}")

# Convert date and time 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.hour

# Clean key columns
df['Age Group'] = pd.cut(df['Age'], bins=[0, 20, 30, 45, 60, 100],
                         labels=['Teen', 'Young Adult', 'Adult', 'Senior', 'Elder'])
df['Customer_Segment'] = df['Customer_Segment'].str.strip()
df['Income'] = df['Income'].str.strip()
df['Order_Status'] = df['Order_Status'].str.strip()
df['Payment_Method'] = df['Payment_Method'].str.strip()

# Ensure numeric columns for plotting
df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce').fillna(0)
df['Total_Amount'] = pd.to_numeric(df['Total_Amount'], errors='coerce').fillna(0)
df['Total_Purchases'] = pd.to_numeric(df['Total_Purchases'], errors='coerce').fillna(0)
df['Hour'] = df['Hour'].fillna(-1)

# --- Seaborn Plot ---
plt.figure(figsize=(9, 6))
sns.violinplot(data=df, x='Customer_Segment', y='Total_Amount', hue='Gender', split=True)
plt.title('Spending Pattern by Segment and Gender')
plt.tight_layout()
plt.savefig('violin_segment_gender.png')
plt.close()

# --- Aggregations ---
sales_by_country = df.groupby('Country')['Total_Amount'].sum().reset_index().sort_values(by='Total_Amount', ascending=False)
segment_income = df.groupby(['Customer_Segment', 'Income'])['Total_Amount'].sum().reset_index()
brand_rating = df.groupby('Product_Brand')['Ratings'].mean().reset_index().sort_values(by='Ratings', ascending=False).head(12)
hourly_distribution = df.groupby('Hour')['Total_Purchases'].sum().reset_index()

# --- Plotly Visuals ---
fig_map = px.choropleth(sales_by_country, locations='Country', locationmode='country names',
                        color='Total_Amount', hover_name='Country',
                        color_continuous_scale='viridis', title='Total Sales by Country')

fig_scatter = px.scatter(df, x='Age', y='Total_Amount', size='Ratings', color='Income',
                         title='Spending by Age and Income Level',
                         hover_data=['Customer_Segment', 'Product_Category'])

fig_heat = px.density_heatmap(df, x='Hour', y='Customer_Segment', z='Total_Amount',
                              histfunc='avg', nbinsx=24, color_continuous_scale='magma',
                              title='Avg Purchase by Hour & Segment')

fig_treemap = px.treemap(segment_income, path=['Customer_Segment', 'Income'],
                         values='Total_Amount', title='Segment vs Income Treemap')

fig_brand = px.bar(brand_rating, x='Product_Brand', y='Ratings', color='Ratings',
                   title='Top 12 Product Brands by Avg Rating')

# --- Dash Dashboard ---
app = dash.Dash(__name__)
app.title = 'Gyanankur Retail Insights'

app.layout = html.Div([
    html.H2('Retail Analytics Dashboard', style={'textAlign': 'center'}),

    dcc.Graph(figure=fig_map),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_heat),
    dcc.Graph(figure=fig_treemap),
    dcc.Graph(figure=fig_brand),

    html.Div(children=[
        html.Img(src='violin_segment_gender.png', style={'width': '60%', 'display': 'block', 'margin': 'auto'}),
        html.P('Gender-based Spending Distribution across Segments', style={'textAlign': 'center'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)

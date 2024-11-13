import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the Excel data
df = pd.read_excel('data.xlsx')

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Interactive Sales Dashboard 📊✨"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
        value=df['Category'].unique()[0],  # Default to the first category
        clearable=False,
        style={'width': '50%'}
    ),
    dcc.Graph(id='sales-profit-graph'),
    dcc.Graph(id='sales-trend')
])

# Define the callbacks for interactivity
@app.callback(
    Output('sales-profit-graph', 'figure'),
    Output('sales-trend', 'figure'),
    Input('category-dropdown', 'value')
)
def update_graphs(selected_category):
    # Filter the data based on the selected category
    filtered_df = df[df['Category'] == selected_category]

    # Sales vs Profit scatter plot
    fig1 = px.scatter(
        filtered_df,
        x='Sales',
        y='Profit',
        color='Category',
        title="Sales vs Profit",
        labels={'Sales': 'Sales Amount', 'Profit': 'Profit Amount'}
    )

    # Sales trend over time
    fig2 = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        title="Sales Trend Over Time",
        labels={'Sales': 'Sales Amount', 'Date': 'Date'}
    )

    return fig1, fig2

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

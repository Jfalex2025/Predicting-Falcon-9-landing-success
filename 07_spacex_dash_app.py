# -*- coding: utf-8 -*-
# Import required libraries
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load SpaceX data into pandas dataframe
# Ensure the dataset spacex_launch_dash.csv is in the same directory
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a Dash application
app = Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Br(),

    # Dropdown for selecting launch site
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True,
        style={'width': '80%', 'margin': 'auto'}
    ),
    html.Br(),

    # Pie chart for success rates
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):", style={'textAlign': 'center'}),

    # Slider for selecting payload range
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=500,
        marks={
            0: '0 kg', 
            2500: '2500 kg', 
            5000: '5000 kg', 
            7500: '7500 kg', 
            10000: '10000 kg'
        },
        value=[min_payload, max_payload]
    ),
    html.Br(),

    # Scatter chart for payload vs. success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Callback for updating the pie chart based on selected site
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(spacex_df, names='Launch Site', values='class',
                     title='Total Successful Launches from All Sites')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        success_counts = filtered_df['class'].value_counts().reindex([0, 1], fill_value=0)
        fig = px.pie(values=success_counts.values, names=['Failure', 'Success'],
                     title=f'Success vs Failure at {selected_site}',
                     color_discrete_map={0: 'red', 1: 'green'})
    return fig

# Callback for updating scatter chart based on selected site and payload range
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     size='Payload Mass (kg)',
                     title='Correlation Between Payload and Success',
                     labels={'class': 'Success (1=Yes, 0=No)'},
                     color_continuous_scale=px.colors.sequential.Viridis)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
 
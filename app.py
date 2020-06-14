import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#d4d1cb',
}

df = pd.read_csv("data.csv")

#Temporary figure, change later
def plot_temp(id_temp):  
	return dcc.Graph(
		id=id_temp,
		figure={
			'data': [
	                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
	                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
	            ],
	            'layout': {
	                'title': id_temp
	            }
	        }
	    )

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def plot1(df):
	agg = df["status_group"].value_counts()
	status_group = list(agg.index)
	status_count = agg.tolist()
	fig = go.Figure(go.Bar(x=status_group,y=status_count))
	return dcc.Graph(figure=fig)

app.layout = html.Div([
	    html.Div([plot1(df)]     ,style = {'width':'30%','float':'left','marginLeft':'2%','marginTop':'2%'}),
	    html.Div([plot_temp("2")],style = {'width':'30%','display': 'inline-block','marginLeft':'3%','marginTop':'2%'}),
	    html.Div([plot_temp("3")],style = {'width':'30%','float':'right','marginRight':'2%','marginTop':'2%'}),
	    html.Div([plot_temp("4")],style = {'width':'30%','float':'left','marginLeft':'2%','marginTop':'2%'}),
	    html.Div([plot_temp("5")],style = {'width':'30%','display': 'inline-block','marginLeft':'3%','marginTop':'2%'}),
	    html.Div([plot_temp("6")],style = {'width':'30%','float':'right','marginRight':'2%','marginTop':'2%'})
	    ],style={'backgroundColor':colors["background"]}
    )

if __name__ == '__main__':
    app.run_server(debug=True)
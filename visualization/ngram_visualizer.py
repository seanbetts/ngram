import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import os

# Load the n-gram probabilities
# Adjust the path to be relative to the project root
ngram_probs = np.load(os.path.join('..', 'dev', 'ngram_probs.npy'))

app = dash.Dash(__name__, static_folder='static')

app.layout = html.Div([
    html.H1("4-gram Language Model Visualizer"),
    html.Div([
        html.Label("Enter 3-letter context:"),
        dcc.Input(id='context-input', type='text', value='', maxLength=3),
    ]),
    dcc.Graph(id='probability-graph')
], className='container')

@app.callback(
    Output('probability-graph', 'figure'),
    Input('context-input', 'value')
)
def update_graph(context):
    if len(context) != 3:
        # If context is not 3 letters, show uniform distribution
        probs = np.ones(27) / 27
    else:
        # Convert context to indices
        indices = [ord(c) - ord('a') for c in context.lower()]
        # Get probabilities for the given context
        probs = ngram_probs[indices[0], indices[1], indices[2]]
    
    # Create bar chart
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '\n']
    trace = go.Bar(x=letters, y=probs)
    
    return {
        'data': [trace],
        'layout': go.Layout(
            title=f'Next Letter Probabilities for Context: "{context}"',
            xaxis={'title': 'Next Letter'},
            yaxis={'title': 'Probability'}
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
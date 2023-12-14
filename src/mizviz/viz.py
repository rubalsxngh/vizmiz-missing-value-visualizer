import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import seaborn as sns
from typing import Type


def vizspectrum(dataframe: Type[pd.DataFrame]):
    '''
    input:
    parameter dataframe: the user-provided data, currently only accepting CSV files

    output:
    color spectrum from white to black
    the darker the color, the fewer missing values a column has.

    for instance, if a column has 10% missing values -> the bar will have a slightly greyish color.
    the darkest color sets the benchmark
    '''

    colors = []  # the initial array having all the column colors as black

    for i, cols in enumerate(dataframe.columns):
        prec = dataframe[cols].isna().mean()
        shade = int(255 * prec)  # Calculate shade based on missing percentage
        color = f'rgb({shade}, {shade}, {shade})'
        colors.append({'color': color, 'opacity': 1-prec})

    fig = go.Figure(data=[go.Bar(
        x=dataframe.columns,
        y=dataframe.notna().sum(),
        marker_color=[color['color'] for color in colors],
        marker=dict(opacity=[color['opacity'] for color in colors]),
        name='missing data spectrum visualizer'
    )])

    fig.update_layout(title='Missing Data Spectrum',
                      xaxis_title='Columns', yaxis_title='Non-Null Count')

    fig.show()

    return fig


def vizbar(dataframe: Type[pd.DataFrame], vizmode='missing'):
    '''
    vizbar is a simple bar chart to visualize missing or actual values.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to visualize.
    - vizmode (str, optional): Visualization mode, either 'missing' or 'actual'. Defaults to 'missing'.

    Returns:
    - fig (plotly.graph_objects.Figure): The Plotly figure object.

    '''

    column_count= {}


    for col in dataframe.columns:
        count=0
        if vizmode== 'missing':
            count= dataframe[col].isna().sum()
        elif vizmode== 'actual':
            count= dataframe[col].notna().sum()
        
        column_count[col]= count

    
    df= pd.DataFrame(list(column_count.items()), columns= ['column', 'count'])
    total_values= dataframe.shape[0]-1

    fig= px.bar(df,
                x= 'column',
                y= 'count',
                title= f"bar graph for count of {'missing' if vizmode== 'missing' else 'actual'} values. \n Total Values: {total_values}",
                labels= {'x': 'Columns', 'y': f"count of {'missing' if vizmode== 'missing' else 'actual'}"},
                color= 'count',
                color_continuous_scale='Blues',
    )

    fig.show()

    return fig


def main():
    df = pd.read_csv(
        'D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
    vizspectrum(df)


if __name__ == '__main__':
    main()

import pandas as pd
import plotly.graph_objects as go
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


def main():
    df = pd.read_csv(
        'D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
    vizspectrum(df)


if __name__ == '__main__':
    main()

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
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

    column_count = {}

    for col in dataframe.columns:
        count = 0
        if vizmode == 'missing':
            count = dataframe[col].isna().sum()
        elif vizmode == 'actual':
            count = dataframe[col].notna().sum()

        column_count[col] = count

    df = pd.DataFrame(list(column_count.items()), columns=['column', 'count'])
    total_values = dataframe.shape[0]-1

    fig = px.bar(df,
                 x='column',
                 y='count',
                 title=f"bar graph for count of {'missing' if vizmode== 'missing' else 'actual'} values. \n Total Values: {total_values}",
                 labels={
                     'x': 'Columns', 'y': f"count of {'missing' if vizmode== 'missing' else 'actual'}"},
                 color='count',
                 color_continuous_scale='Blues',
                 )


    return fig


def heatmap(dataframe: Type[pd.DataFrame]):
    """
    Generates a heatmap using Plotly to visualize missing values in a DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to visualize.

    Returns:
    - fig: a matplotlib Figure.

    visualize: The more white the heatmap-> more the missing values in dataframe.
    - a white bar in heatmap means that cell has missing value.
    """

    null_mask = dataframe.notna()

    ax = sns.heatmap(null_mask, cmap='binary', cbar=False, annot=False)
    plt.title('Missing Values Heatmap, white displays missing values')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.show()

    fig = ax.get_figure()

    return fig


def vdendrogram(df: Type[pd.DataFrame]):
    '''
    Generates a dendrogram using scipy's Agglomerative Clustering Algorithm( Single linkage).

    Parameters:
    - df (pd.DataFrame): The DataFrame to visualize. This is the input DataFrame that will be used to generate the dendrogram.

    Returns:
    - fig: a matplotlib Figure. The function doesn't explicitly return a value, but it generates a plot.

    Visualization Explanation:
    - Convert non-numeric values to numeric or boolean: This step is crucial to create a binary matrix,
        - indicating the presence (1) or absence (0) of missing values.

    - Transpose the binary matrix for clustering variables: 
        - Hierarchical clustering is applied to the transpose of the binary matrix. 
        - Each column represents a variable, and each row represents an observation.

    - Perform hierarchical clustering: The agglomerative hierarchical clustering algorithm is used with the ward method to measure the distance between clusters.

    - Create a dendrogram: The dendrogram is a tree-like diagram that visually represents the results of hierarchical clustering. It shows how variables are grouped based on their missing data patterns.

    - Display the plot: Finally, the dendrogram plot is shown using matplotlib.

    Note: The function is designed to be used as a tool for visual exploration and understanding of missing data patterns in the input DataFrame.
    '''

    df_mask = df.notna().astype('int')

    simple_linkage_cluster = linkage(df_mask.transpose(), 'single', 'jaccard')

    plt.figure()

    dendrogram(simple_linkage_cluster, labels=df_mask.columns)

    plt.xlabel('Columns in dataset')

    plt.ylabel('Co- relation between columns missing values')

    plt.title('Dendogram using single linkage hierrachical clustering.')

    plt.show()

    fig = plt.gcf()

    return fig


def main():
    df = pd.read_csv(
        'D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
    vizspectrum(df)


if __name__ == '__main__':
    main()

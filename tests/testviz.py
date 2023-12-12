from vizualizer import viz
import pandas as pd

df= pd.read_csv('D:/my_projects/vizmiz/data/baby_names.csv')
viz.vizspectrum(df)


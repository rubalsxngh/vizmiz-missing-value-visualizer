from vizualizer import viz
import plotly.graph_objects as go
import pandas as pd

import unittest


class test_spec_visualizer(unittest.TestCase):
    def test_spec(self):
        df= pd.read_csv('D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
        
        self.assertIsInstance(viz.vizspectrum(df), go.Figure)

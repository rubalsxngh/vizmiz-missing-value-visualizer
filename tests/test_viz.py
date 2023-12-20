from src.mizviz import viz
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

import unittest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class test_spec_visualizer(unittest.TestCase):
    def test_spec(self):
        df= pd.read_csv('D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
        '''
        this test use sample dataset from /data repo, can replace it with you own
        '''
        
        self.assertIsInstance(viz.vizspectrum(df), go.Figure)


class test_bar_visualizer(unittest.TestCase):
    def test_bar(self):
        df= pd.read_csv('D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
        '''
        this test use sample dataset from /data repo, can replace it with you own
        '''

        self.assertIsInstance(viz.vizbar(df), go.Figure)

class test_heatmap_visualizer(unittest.TestCase):
    def test_heatmap(self):
        df= pd.read_csv('D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
        '''
        this test use sample dataset from /data repo, can replace it with you own
        '''

        self.assertIsInstance(viz.heatmap(df), plt.Figure)


class test_dendogram_visualizer(unittest.TestCase):
    def test_dendogram(self):
        df= pd.read_csv('D:/my_projects/vizmiz-missing-value-visualizer/data/baby_names.csv')
        '''
        this test use sample dataset from /data repo, can replace it with you own
        '''

        self.assertIsInstance(viz.vdendrogram(df), plt.Figure)
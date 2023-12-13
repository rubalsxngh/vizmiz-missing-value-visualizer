# mizviz-missing-value-visualizer
VizMiz is a Python library for visualizing missing data in pandas DataFrames.

## Installation

You can install VizMiz using pip:

   ```bash
   pip install -i https://test.pypi.org/simple/ mizviz==0.0.1
   ```

## Usage

Use the vizspectrum function to visualize missing data:

   ```bash
   import pandas as pd
   from mizviz import viz
   df = pd.read_csv('path/to/your/data.csv')
   viz.vizspectrum(df)
   ```

## Features

- Color spectrum visualization for missing values
- Customizable color scales for improved visibility
- Integration with Plotly for interactive and dynamic visualizations


## Contributing
Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.
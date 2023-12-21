# mizviz-missing-value-visualizer
VizMiz is a Python library for visualizing missing data in pandas DataFrames.

## Installation

You can install VizMiz using pip:

   ```bash
   pip install mizviz
   ```

You can install other required dependencies running:

   ```
   pip install -r requirements.txt
   ```

## Usage

Use the vizspectrum function to visualize missing data:

   ```bash
   import pandas as pd
   from mizviz import viz
   df = pd.read_csv('path/to/your/data.csv')
   fig= viz.vizspectrum(df)
   fig.show()
   ```

Use the vizbar function to visualize missing or actual( non-missing data) using simple bar:

   ```
   import pandas as pd
   from mizviz import viz
   df = pd.read_csv('path/to/your/data.csv')
   fig= viz.vizbar(df, 'missing') #create a bar graph for missing values( default)
   fig= viz.vizbar(df, 'actual') #create a bar graph for actual values

   fig.show()
   ```

Use the heatmap function to visualize missing data using a heatmap:

   ```
   import pandas as pd
   from mizviz import viz
   df = pd.read_csv('path/to/your/data.csv')
   viz.heatmap(df) #create a heatmap: more white the heatmap is, more missing values dataframe contains
   ```

Use the vdendrogram function to visualize missing data using a dendogram:

   ```
   import pandas as pd
   from mizviz import viz
   df = pd.read_csv('path/to/your/data.csv')
   viz.vdendrogram(df) #create a dendrogram: provides co-relation between columns considering missing values
   ```


## Features

- Color spectrum visualization for missing values
- Customizable color scales for improved visibility
- Integration with Plotly for interactive and dynamic visualizations


## Contributing
Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.

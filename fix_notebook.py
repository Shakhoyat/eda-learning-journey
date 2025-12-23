import json

# Read the notebook
with open(r'e:\eda-learning-journey\Time series\Forecasting_using_Fbprophet.ipynb', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix the widgets metadata
widgets = data['metadata']['widgets']

# Remove incorrectly placed state key if exists
if 'state' in widgets:
    del widgets['state']

# Get the widget data
widget_data = widgets.get('application/vnd.jupyter.widget-state+json', {})

# Restructure: wrap widget data under 'state' key
widgets['application/vnd.jupyter.widget-state+json'] = {
    'state': widget_data
}

# Write back
with open(r'e:\eda-learning-journey\Time series\Forecasting_using_Fbprophet.ipynb', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print('Fixed! Restructured widgets metadata with proper state key.')

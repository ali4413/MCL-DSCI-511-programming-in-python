import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# First, rename the column capture_rt to capture_rate
# Create a new column named AD_total 
# by adding the attack and defense columns from the pokemon dataset
# Finally use .plot.scatter() to plot AD_total on the x-axis 
# and capture_rt on the y-axis
# Name the full chain pokemon_plot
# Use a new line for each method

pokemon_plot = (pokemon.rename(columns={'capture_rt': 'capture_rate'})
                       .assign(AD_total=pokemon['defense'] + pokemon['defense'])
                       .plot.scatter(x='AD_total', y='capture_rate')
                )



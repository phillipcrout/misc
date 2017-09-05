import numpy as np
import pandas as pd

df = pd.read_csv('~/git/athletics/ordered_data_as_csv.csv')

### Top 16 in each event in 2016 ###

df_2016 = df[df.year==2016]
del df_2016['year']

### Cut down to 16 per event

df_dist_mean = []
for x in df.distance.unique():    
    df_dist_mean.append(df_2016.time_in_seconds[df_2016.distance==x].mean())
    ## add in std


"""
### Top athlete in each year between 2000 and 2016, by event
### Trends over time (?new file)
"""
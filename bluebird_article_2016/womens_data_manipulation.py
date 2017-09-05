import numpy as np
import pandas as pd


input_data = pd.read_csv('~/git/athletics/full_data_as_csv.csv')

def convert_to_seconds(time):
    time = time[0:7]  #this catch results with suffixed A (possibly for altitude)
    mins = float(time.split(':')[0])
    secs = float(time.split(':')[1])
    return mins*60+secs
    
input_data['time_in_seconds'] = input_data.time.apply(convert_to_seconds)

def get_top_performances(df):
    ## Order by time_in_seconds
    df.sort_values(by='time_in_seconds',inplace=True)
    ## Drop duplicates on all columns except time,time_in_seconds - keep first
    df.drop_duplicates(['first_name','second_name','year','distance'],inplace=True)    
    return df
    
ordered = get_top_performances(input_data)

ordered.to_csv('~/git/athletics/ordered_data_as_csv.csv',index=False)

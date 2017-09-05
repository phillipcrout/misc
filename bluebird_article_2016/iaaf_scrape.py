from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd
import urllib.request

def cut_to_50(list):
    return list[0:50]

## Start empty dataframe ###
main_df = pd.DataFrame(columns=['first_name','second_name','time','year','distance'])

start = 'https://www.iaaf.org/records/toplists/middle-long/'
end = '/outdoor/women/senior/'

## get a list of strings of potential years
years_strings = [str(x) for x in list(np.arange(2000,2017,1))] #up to 2016
    

for distance in ['800-metres','1500-metres','3000-metres-steeplechase','5000-metres','10000-metres']:
    for year in years_strings:
            raw_pull = urllib.request.urlopen(start+distance+end+year).read()
            soup = BeautifulSoup(raw_pull,"lxml") #ubuntu windows compat is ?!
            marks = soup.find_all(attrs={"data-th":"Mark"})
            names = soup.find_all(attrs={"data-th":"Competitor"})

            fn,sn,y = [],[],[]

            for x in names: 
                sn.extend(x.find('a').find('span').contents)
                fn.append(x.find('a').contents[0])

            for x in marks:
                y.extend((x.contents)) #gets the times
                
            i=0
            while i < len(y):
                y[i] = y[i].strip()
                i+=1

            fn,sn,y = cut_to_50(fn),cut_to_50(sn),cut_to_50(y)

            d = {'first_name': fn, 'second_name': sn,'time':y}
            df = pd.DataFrame(data=d)
            df['year']=year
            df['distance']=distance
            main_df = pd.concat([main_df,df])

### Final dataframe size is (4000,5)
## Runtime ~ 5 minutes

main_df.to_csv('./full_data_as_csv.csv',quoting=csv.QUOTE_ALL,index=False)

#  main_df.to_pickle('./full_results_list')
## Throws an error as maximum recursion depth is exceeded.

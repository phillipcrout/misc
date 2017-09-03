from monzo.monzo import Monzo # Import Monzo Class
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns #for the nicer default styles

from secret_string import *

client = Monzo(secret_string) # Replace access token with a valid token found at: https://developers.getmondo.co.uk/
account_id = client.get_first_account()['id'] # Get the ID of the first account linked to the access token

"""
## Demo 
balance = client.get_balance(account_id) # Get your balance object
print(balance['balance']) # 100000000000
print(balance['currency']) # GBP
print(balance['spend_today']) # 2000
"""

transactions = client.get_transactions(account_id)['transactions']
col = ['amount','include_in_spending','notes','category']
df = pd.DataFrame(data=transactions)[col]

def clean_for_pie(df):
    df_neg = df[df.amount<0]
    df_gr  = df_neg.groupby('category').sum()
    df_gr = df_gr*-1
    return df_gr
    
dfx = clean_for_pie(df)
plt.pie(dfx.amount[dfx.index!='entertainment'],labels=dfx.index[dfx.index!='entertainment'])
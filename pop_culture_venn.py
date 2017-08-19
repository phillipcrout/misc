from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import *
import pandas as pd

T = pd.Series(['Alcohol','Parent Child','Man','Sidekick','Subsiduary'])
A = pd.Series([1,1,1,0,1])
R   = pd.Series([1,1,1,1,1])
B = pd.Series([1,1,1,1,0])

df = pd.DataFrame({'theme':T,'Archer':A,'Rick':R,'Bojack':B})

A = set(df.theme[df.Archer==1]) #Archer
B = set(df.theme[df.Rick==1]) #Rick
C = set(df.theme[df.Bojack==1])  #BoJack

v = venn3_unweighted([A,B,C], ('Archer', 'R&M', 'BoJack'))

#v.get_label_by_id('100').set_text('\n'.join(A-B-C))
v.get_label_by_id('110').set_text('\n'.join(A&B-C))
v.get_label_by_id('011').set_text('\n'.join(B&C-A))
v.get_label_by_id('101').set_text('\n'.join(A&C-B))
v.get_label_by_id('111').set_text('\n'.join(A&B&C))
#v.get_label_by_id('011').set_text('\n'.join(B&C-A))

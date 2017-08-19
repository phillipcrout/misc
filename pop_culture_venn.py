from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import *

A = set(['Alcohol','Parent Child','Man','Subsiduary','Spys']) #Archer
B = set(['Alcohol','Parent Child','Man','Sidekick','Subsiduary','Science']) #Rick
C = set(['Alcohol','Parent Child','Man','Sidekick','Acting'])  #BoJack

v = venn3_unweighted([A,B,C], ('Archer', 'R&M', 'BoJack'))

#v.get_label_by_id('100').set_text('\n'.join(A-B-C))
v.get_label_by_id('110').set_text('\n'.join(A&B-C))
v.get_label_by_id('011').set_text('\n'.join(B&C-A))
v.get_label_by_id('101').set_text('\n'.join(A&C-B))
v.get_label_by_id('111').set_text('\n'.join(A&B&C))
#v.get_label_by_id('011').set_text('\n'.join(B&C-A))

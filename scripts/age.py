import pandas as pd
from os import path

data_path = path.abspath('/usr/share/opfvta_bidsdata/participants.tsv')
df = pd.read_csv(data_path, sep='\t')

mean_age = round(df['age [d]'].mean())
std_age = round(df['age [d]'].std())
print('{} days (standard deviation {} days)'.format(mean_age,std_age))

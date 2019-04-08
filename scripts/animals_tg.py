import pandas as pd
from os import path

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('data/groups.csv')
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')
wt_animals = df.loc[(df['Genotype_code']=='datg') & (df['Mean VTA t'].notnull()),'Subject'].unique()
print(len(wt_animals))

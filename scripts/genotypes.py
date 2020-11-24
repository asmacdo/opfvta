import pandas as pd
from os import path

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('data/groups.csv')
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')
tg_animals = df.loc[(df['Genotype_code']=='datg') & (df['Mean VTA t'].notnull()),'Subject'].unique()
wt_animals = df.loc[(df['Genotype_code']=='dawt') & (df['Mean VTA t'].notnull()),'Subject'].unique()

tg_animals=len(tg_animals)
wt_animals=len(wt_animals)

output_template='{tg_animals} transgenic animals and {wt_animals} wild type control animals'
output = output_template.format(
	tg_animals=tg_animals,
	wt_animals=wt_animals,
	)

print(output)

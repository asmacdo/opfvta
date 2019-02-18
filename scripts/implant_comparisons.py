import pandas as pd
import matplotlib as mpl
from os import path
from scipy import stats
from itertools import product

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('data/groups.csv')
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')

df = df.loc[df['Task Category'] == 'Block']
# do not take into account unimplanted animals
df = df[pd.notnull(df['PA rel. Bregma [mm]'])]

pas = df['PA rel. Bregma [mm]'].unique()
#for pa in pas:
#	values = df.loc[df['PA rel. Bregma [mm]']==pa, 'Mean VTA t'].tolist()
#	p = stats.ttest_1samp(values, 0).pvalue
#	print(pa, p, p*len(pas))

depths = df['Depth rel. skull [mm]'].unique()
#for depth in depths:
#	values = df.loc[df['Depth rel. skull [mm]']==depth, 'Mean VTA t'].tolist()
#	p = stats.ttest_1samp(values, 0).pvalue
#	print(depth, p, p*len(depths))

for depth, pa in product(depths,pas):
	my_slice = df.loc[(df['PA rel. Bregma [mm]'] == pa) & (df['Depth rel. skull [mm]'] == depth)]
	values = my_slice['Mean VTA t'].tolist()
	p = stats.ttest_1samp(values, 0).pvalue
	print(depth,pa,p)

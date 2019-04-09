import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
from seaborn import swarmplot

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

groups_path = path.abspath('data/groups.csv')
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')

df = df.loc[df['Task Category'] != 'Tonic']
df = df.loc[df['Genotype_code'] == 'datg']
# do not take into account unimplanted animals
df = df[pd.notnull(df['PA rel. Bregma [mm]'])]

df['Implant PA/Depth'] = df['PA rel. Bregma [mm]'].map(str) +'/'+ df['Depth rel. skull [mm]'].map(str)

ax = swarmplot(
	hue="Implant PA/Depth",
	x="Task Category",
	y='Mean VTA t',
	data=df,
	)

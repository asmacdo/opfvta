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

df = df.loc[df['Genotype_code'] == 'datg']
# do not take into account unimplanted animals
df = df[pd.notnull(df['PA rel. Bregma [mm]'])]
df = df[pd.notnull(df['Mean VTA t'])]

ax = swarmplot(
	x="PA rel. Bregma [mm]",
	hue="Depth rel. skull [mm]",
	y='Mean VTA t',
	data=df,
	size=mpl.rcParams['lines.markersize'],
	)
plt.ylabel('')
ax.tick_params(labelleft=False)

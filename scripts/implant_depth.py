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

# do not take into account unimplanted animals
df = df[pd.notnull(df['PA rel. Bregma [mm]'])]

ax = swarmplot(
	x="Depth rel. skull [mm]",
	hue="PA rel. Bregma [mm]",
	y='Mean VTA t',
	data=df,
	)

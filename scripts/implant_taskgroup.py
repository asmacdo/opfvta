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

df['Task Category'] = df['Task']
task_categories = {
	'CogBr':'Block',
	'CogBm':'Block',
	'CogMwf':'Block',
	'CogB':'Block',
	'JPogP':'Phasic',
	'CogP':'Phasic',
	'JPogT':'Tonic',
	}
df = df.replace({'Task Category': task_categories})
df = df.loc[df['Task Category'] != 'Tonic']

ax = swarmplot(
	x="OrthogonalStereotacticTarget_code",
	hue="Task Category",
	y='Mean VTA t',
	data=df,
	)
plt.xticks(rotation=90)

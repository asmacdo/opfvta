import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
from seaborn import swarmplot

data_path = path.abspath('data/functional_significance.csv')
df = pd.read_csv(data_path)

#df.loc[df['Processing']=='Unprocessed', 'Template'] = ''
ax = swarmplot(
	x="Subject",
	y='Mean VTA Significance',
	data=df,
	hue="Task",
	)
plt.xticks(rotation=90)
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
from seaborn import swarmplot

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

ax = swarmplot(
	x="Task",
	y='Mean VTA t',
	data=df,
	hue="Subject",
	)
plt.xticks(rotation=90)

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from os import path
from itertools import product
from seaborn import swarmplot

data_path = path.abspath('data/functional_t.csv')
df = pd.read_csv(data_path)

ax = swarmplot(
	x="Subject",
	y='Mean VTA t',
	data=df,
	hue="Task",
	)
plt.xticks(rotation=90)

import json
import matplotlib as mpl
import pandas as pd
import seaborn as sns

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_rois = [float(i) for i in correlation_data['regionwise']['functional']]
img2_rois = [float(i) for i in correlation_data['regionwise']['structural']]

df = pd.DataFrame(
	{
		'Functional Mean ROI t': img1_rois,
		'Structural Mean ROI t': img2_rois,
		}
	)

linewidth = mpl.rcParams['lines.linewidth']
g = sns.regplot('Functional Mean ROI t', 'Structural Mean ROI t',
	ci=99,
	data=df,
	color="tab:blue",
	scatter_kws={'s':linewidth*10},
	)

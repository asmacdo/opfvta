import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from lib.utils import float_to_tex

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_rois = [float(i) for i in correlation_data['regionwise']['functional']]
img2_rois = [float(i) for i in correlation_data['regionwise']['structural']]

r_rois, p_rois = stats.pearsonr(img1_rois, img2_rois)

r_rois_tex = float_to_tex(r_rois)
p_rois_tex = float_to_tex(p_rois)

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
	line_kws={
		'label':'$\mathrm{{\\rho={}\;(p={})}}$'.format(r_rois_tex,p_rois_tex),
		},
	)

legend = plt.legend(handletextpad=0.0, handlelength=0,markerscale=0)

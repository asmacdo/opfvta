import json
import matplotlib as mpl
import pandas as pd
import seaborn as sns

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_voxels = [float(i) for i in correlation_data['voxelwise']['functional']]
img2_voxels = [float(i) for i in correlation_data['voxelwise']['structural']]

df = pd.DataFrame(
	{
		'Functional Voxel t': img1_voxels,
		'Structural Voxel t': img2_voxels,
		}
	)

linewidth = mpl.rcParams['lines.linewidth']
g = sns.regplot('Functional Voxel t', 'Structural Voxel t',
	ci=99,
	data=df,
	color="tab:gray",
	scatter_kws={'s':linewidth},
	)

import json
import pandas as pd
import seaborn as sns

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_voxels = [float(i) for i in correlation_data['voxelwise']['functional']]
img2_voxels = [float(i) for i in correlation_data['voxelwise']['structural']]

df = pd.DataFrame(
	{
		'functional': img1_voxels,
		'structural': img2_voxels,
		}
	)

g = sns.jointplot('functional', 'structural',
	data=df,
	kind="reg",
	color="m",
	)

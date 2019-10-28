import json
import pandas as pd
import seaborn as sns

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_rois = [float(i) for i in correlation_data['regionwise']['functional']]
img2_rois = [float(i) for i in correlation_data['regionwise']['structural']]

df = pd.DataFrame(
	{
		'functional': img1_rois,
		'structural': img2_rois,
		}
	)

g = sns.jointplot('functional', 'structural',
	data=df,
	kind="reg",
	color="m",
	)
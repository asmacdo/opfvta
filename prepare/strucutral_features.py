import os
import pandas as pd
from samri.fetch.local import prepare_feature_map

df = pd.read_csv('../data/structural_features.csv')

region_data_template = '/usr/share/ABI-connectivity-data/Ventral_tegmental_area-{}/'
target_path_template = '~/.scratch/opfvta/structural_features/sub-{}/ses-1/anat/vta.nii.gz'

region_data_template = os.path.abspath(os.path.expanduser(region_data_template))
target_path_template = os.path.abspath(os.path.expanduser(target_path_template))
for ix, row in df.iterrows():
	identifier = row['identifier']
	print(identifier)
	invert = row['laterality'] == 'right'
	prepare_feature_map(region_data_template.format(identifier),
		invert_lr=invert,
		save_as=target_path_template.format(identifier)
		)

import os
import pandas as pd
from samri.fetch.local import prepare_feature_map
from samri.utilities import bids_autofind_df

scratch_dir = '~/.scratch/opfvta'

df = pd.read_csv('../data/features_structural.csv')

region_data_template = '/usr/share/ABI-connectivity-data/Ventral_tegmental_area-{}/'
target_path_template = '~/.scratch/opfvta/features_normalized/sub-{my_id}/ses-1/anat/sub-{my_id}_ses-1_cope.nii.gz'

region_data_template = os.path.abspath(os.path.expanduser(region_data_template))
target_path_template = os.path.abspath(os.path.expanduser(target_path_template))
for ix, row in df.iterrows():
	identifier = row['identifier']
	invert = row['laterality'] == 'left'
	prepare_feature_map(region_data_template.format(identifier),
		invert_lr=invert,
		scaling='normalize',
		save_as=target_path_template.format(my_id=identifier)
		)

df = bids_autofind_df('{}/l1/'.format(scratch_dir),
	path_template='sub-{{subject}}/ses-{{session}}/'\
		'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_{{modality}}_betas.nii.gz',
	match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/'\
		'.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_(?P<modality>cbv|bold)_betas\.nii\.gz',
	)
for ix, row in df.iterrows():
	beta_path = row['path']
	feature_path = beta_path.replace('_betas.','_cope.')
	feature_path = feature_path.replace('/l1/','/features_normalized/')
	prepare_feature_map(beta_path,
		scaling='normalize',
		save_as=feature_path,
		)

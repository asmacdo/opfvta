import os
import pandas as pd
from samri.fetch.local import prepare_abi_connectivity_maps, prepare_feature_map
from samri.fetch.model import abi_connectivity_map
from samri.utilities import bids_autofind_df

scratch_dir = '~/.scratch/opfvta'

#selection in once place to avoid divergence
df = pd.read_csv('../data/features_structural.csv')
invert_lr_experiments = df.loc[df['laterality']=='left', 'identifier'].tolist()
invert_lr_experiments = [str(i) for i in invert_lr_experiments]

# Create normalized features
target_path_template = '~/.scratch/opfvta/features_normalized/sub-{experiment}/ses-1/anat/sub-{experiment}_ses-1_cope.nii.gz'

## ABI connectivity
target_path_template = os.path.abspath(os.path.expanduser(target_path_template))
prepare_abi_connectivity_maps('ventral_tegmental_area',
	invert_lr_experiments=invert_lr_experiments,
	reposit_path=target_path_template,
	scaling='normalize',
	)

# Compute cumulative map for all projections
abi_connectivity_map('ventral_tegmental_area',
	invert_lr_experiments=invert_lr_experiments,
	#exclude_experiments=df.loc[df['exclude'], 'identifier'].tolist(),
	save_as_zstat='../data/vta_projection_zstat.nii.gz',
	save_as_tstat='../data/vta_projection_tstat.nii.gz',
	save_as_cope='../data/vta_projection_cope.nii.gz',
	)

## Functional data
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

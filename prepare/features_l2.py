from samri.pipelines import glm
from os import path
import pandas as pd
import numpy as np

scratch_dir = '~/.scratch/opfvta'
seed_base = '{}/seed_l1/'.format(scratch_dir)

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)
groups['D/PA'] = list(zip(
	groups['Depth rel. skull [mm]'],
	groups['PA rel. Bregma [mm]']
	))

# Per stimulation category classification
## Block
coordinates_path = path.abspath('../data/implant_coordinates_block.csv')
coordinates = pd.read_csv(coordinates_path)
best_coordinates = coordinates.loc[coordinates['Best Cluster']==True]
best_coordinates['D/PA'] = list(zip(
	best_coordinates['Depth rel. skull [mm]'],
	best_coordinates['PA rel. Bregma [mm]']
	))
dpas = best_coordinates['D/PA'].tolist()

filtered_group = groups.loc[
	(groups['D/PA'].isin(dpas)) &
	(groups['Genotype_code']=='datg')
	]
other_group = groups.loc[
	(~groups['D/PA'].isin(dpas)) &
	(groups['Genotype_code']=='datg')
	]
control_group = groups.loc[
	(groups['Genotype_code']=='dawt')
	]
filtered_animals = [str(i) for i in filtered_group['Subject'].tolist()]
other_animals = [str(i) for i in other_group['Subject'].tolist()]
control_animals = [str(i) for i in control_group['Subject'].tolist()]

##############################################################################
glm.l2_controlled_effect('~/.scratch/opfvta/features_normalized',
	workflow_name='features_l2',
	out_dir='{}/features_l2'.format(scratch_dir),
	mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':filtered_animals,'type':[np.nan]},
	control_match={'type':['anat']},
	run_mode='fe',
	keep_work=True,
	)

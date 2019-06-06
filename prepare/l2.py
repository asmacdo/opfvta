from os import path
from samri.pipelines import glm
import pandas as pd
import portage

prefix = portage.root
scratch_dir = '~/.scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)
seed_base = '{}/seed_l1/'.format(scratch_dir)

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='task',
	n_jobs_percentage=.33,
	out_base=scratch_dir,
	)

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

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'block_filtered'},
		{'subject':other_animals, 'alias':'block_other'},
		{'subject':control_animals, 'alias':'block_control'},
		],
	run_mode='fe',
	)
glm.l2_controlled_effect(l1_base,
	workflow_name='alias-block_filtered_controlled',
	out_dir='{}/l2/alias-block_filtered_controlled'.format(scratch_dir),
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':filtered_animals},
	control_match={'subject':control_animals},
	run_mode='fe',
	)
glm.l2_controlled_effect(l1_base,
	workflow_name='alias-block_other_controlled',
	out_dir='{}/l2/alias-block_other_controlled'.format(scratch_dir),
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':other_animals},
	control_match={'subject':control_animals},
	run_mode='fe',
	)
glm.l2_common_effect(seed_base,
	workflow_name='seed_l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'block_filtered'},
		{'subject':other_animals, 'alias':'block_other'},
		{'subject':control_animals, 'alias':'block_control'},
		],
	run_mode='fe',
	)
glm.l2_controlled_effect(seed_base,
	workflow_name='alias-block_filtered_controlled',
	out_dir='{}/seed_l2/alias-block_filtered_controlled'.format(scratch_dir),
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':filtered_animals},
	control_match={'subject':control_animals},
	run_mode='fe',
	)


## Phasic
coordinates_path = path.abspath('../data/implant_coordinates_phasic.csv')
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

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'CogBl',
		'CogBr',
		'CogMwf',
		'CogBr',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'phasic_filtered'},
		{'subject':other_animals, 'alias':'phasic_other'},
		],
	run_mode='fe',
	)
glm.l2_common_effect(seed_base,
	workflow_name='seed_l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'CogBl',
		'CogBr',
		'CogMwf',
		'CogBr',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'phasic_filtered'},
		{'subject':other_animals, 'alias':'phasic_other'},
		],
	run_mode='fe',
	)

# Stimulus-protocol agnostic classification
coordinates_path = path.abspath('../data/implant_coordinates.csv')
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

glm.l2_common_effect(l1_base,
	workflow_name='l2_',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'block_filtered'},
		{'subject':other_animals, 'alias':'block_other'},
		],
	run_mode='fe',
	)
glm.l2_common_effect(l1_base,
	workflow_name='l2_',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'CogBl',
		'CogBr',
		'CogMwf',
		'CogBr',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'phasic_filtered'},
		{'subject':other_animals, 'alias':'phasic_other'},
		],
	run_mode='fe',
	)
glm.l2_controlled_effect(l1_base,
	workflow_name='alias-block_filtered_controlled',
	out_dir='{}/l2_/alias-block_filtered_controlled'.format(scratch_dir),
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':filtered_animals},
	control_match={'subject':control_animals},
	run_mode='fe',
	)
glm.l2_controlled_effect(l1_base,
	workflow_name='alias-block_other_controlled',
	out_dir='{}/l2_/alias-block_other_controlled'.format(scratch_dir),
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	match={'subject':other_animals},
	control_match={'subject':control_animals},
	run_mode='fe',
	)
glm.l2_common_effect(seed_base,
	workflow_name='seed_l2_',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'block_filtered'},
		{'subject':other_animals, 'alias':'block_other'},
		],
	run_mode='fe',
	)
glm.l2_common_effect(seed_base,
	workflow_name='seed_l2_',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'CogBl',
		'CogBr',
		'CogMwf',
		'CogBr',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'phasic_filtered'},
		{'subject':other_animals, 'alias':'phasic_other'},
		],
	run_mode='fe',
	)

# Manual classification
filtered_group = groups.loc[
	(groups['PA rel. Bregma [mm]'] >= -3.2)
	]
other_group = groups.loc[
	(groups['PA rel. Bregma [mm]'] <= -3.3)
	]
filtered_animals = [str(i) for i in filtered_group['Subject'].tolist()]
other_animals = [str(i) for i in other_group['Subject'].tolist()]

glm.l2_common_effect(l1_base,
	workflow_name='l2Manual',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'block_filtered'},
		{'subject':other_animals, 'alias':'block_other'},
		],
	run_mode='fe',
	)

# No classification
animals = [str(i) for i in groups['Subject'].tolist()]
glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':animals, 'alias':'block'},
		],
	run_mode='fe',
	)

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':[
		'CogBl',
		'CogBr',
		'CogMwf',
		'CogBr',
		],},
	out_base=scratch_dir,
	target_set=[
		{'subject':animals, 'alias':'phasic'},
		],
	run_mode='fe',
	)

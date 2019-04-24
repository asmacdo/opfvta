from os import path
from samri.pipelines import glm
import pandas as pd
import portage

prefix = portage.root
scratch_dir = '~/.scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)

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
	)

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
	)

# manual classification

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
	)

glm.l2_common_effect(l1_base,
	workflow_name='l2Manual',
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
	)

# no classification

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
	)

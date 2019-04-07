from os import path
from samri.pipelines import glm
import pandas as pd
import portage

prefix = portage.root
scratch_dir = '~/.scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)

coordinates_path = path.abspath('../data/implant_coordinates.csv')
coordinates = pd.read_csv(coordinates_path)
coordinates = coordinates.loc[coordinates['Best Cluster']==True]
pas = coordinates['PA rel. Bregma [mm]'].tolist()
depths = coordinates['Depth rel. skull [mm]'].tolist()

filtered_group = groups.loc[
	(groups['Depth rel. skull [mm]'].isin(depths)) &
	(groups['PA rel. Bregma [mm]'].isin(pas)) &
	(groups['Genotype_code']=='datg')
	]
other_group = groups.loc[
	(~groups['Depth rel. skull [mm]'].isin(depths)) &
	(~groups['PA rel. Bregma [mm]'].isin(pas)) &
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
	groupby='task',
	n_jobs_percentage=.33,
	out_base=scratch_dir,
	)

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	exclude={'task':['JPogP','CogP'],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals, 'alias':'filtered'},
		{'subject':other_animals, 'alias':'other'},
		{'subject':control_animals, 'alias':'control'},
		],
	)

from os import path
from samri.pipelines import glm
import pandas as pd

scratch_dir = '~/data_scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)

filtered_groups = groups.loc[
	(groups['Depth rel. skull [mm]'] >= 4.4) &
	(groups['PA rel. Bregma [mm]'] >= -3.3)
	]
filtered_animals = filtered_groups['Subject'].tolist()
other_animals = groups.loc[~groups['Subject'].isin(filtered_animals), 'Subject'].tolist()

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='/home/hioanas/gentoo/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	groupby='subject_set',
	n_jobs_percentage=.33,
	#The JPogT task in the current data has only one run, and cannot be modelled at the second level.
	exclude={'task':['JPogT'],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals},
		{'subject':other_animals},
		],
	)

#glm.l2_common_effect(l1_base,
#	workflow_name='l2',
#	mask='/home/hioanas/gentoo/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
#	groupby='task',
#	n_jobs_percentage=.33,
#	#The JPogT task in the current data has only one run, and cannot be modelled at the second level.
#	exclude={'task':['JPogT'],},
#	out_base=scratch_dir,
#	)

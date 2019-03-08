from os import path
from samri.pipelines import glm
import pandas as pd
import portage

<<<<<<< HEAD
=======
prefix = portage.root
>>>>>>> 127cead7c7a647f96c9c182d41e66c6090f8b5e2
scratch_dir = '~/.scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)

filtered_groups = groups.loc[
	(groups['Depth rel. skull [mm]'] >= 4.4) &
	(groups['PA rel. Bregma [mm]'] >= -3.3)
	]
filtered_animals = [str(i) for i in filtered_groups['Subject'].tolist()]
other_animals = [str(i) for i in groups.loc[~groups['Subject'].isin(filtered_animals), 'Subject'].tolist()]

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='task',
	n_jobs_percentage=.33,
	#The JPogT task in the current data has only one run, and cannot be modelled at the second level.
	exclude={'task':['JPogT'],},
	out_base=scratch_dir,
	)

glm.l2_common_effect(l1_base,
	workflow_name='l2',
	mask='{}usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
	groupby='subject_set',
	n_jobs_percentage=.33,
	#Only considering block stimulation (filtering out tonic and phasic stimulation).
	exclude={'task':['JPogT','JPogP','CogP'],},
	out_base=scratch_dir,
	target_set=[
		{'subject':filtered_animals},
		{'subject':other_animals},
		],
	)


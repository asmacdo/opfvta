from samri.pipelines import glm
from os import path
import pandas as pd
import numpy as np

scratch_dir = '~/.scratch/opfvta'

glm.l2_common_effect('~/.scratch/opfvta/features_normalized',
	workflow_name='projection',
	mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	n_jobs_percentage=.33,
	exclude={'task':[
		'JPogP',
		'CogP',
		],},
	out_base=scratch_dir,
	include={'type':['anat']},
	run_mode='fe',
	)

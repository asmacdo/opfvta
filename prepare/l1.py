from os import path
from samri.pipelines import glm
from samri.pipelines.glm import seed

scratch_dir = '~/.scratch/opfvta'

preprocess_base = path.join(scratch_dir,'preprocess')

seed(preprocess_base,'../data/vta_right.nii.gz',
	mask='mouse',
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	out_base=scratch_dir,
	workflow_name='seed_vta_right',
	)

glm.l1(preprocess_base,
	bf_path='../data/chr_beta1.txt',
	habituation=None,
	mask='mouse',
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1',
	out_base=scratch_dir,
	)

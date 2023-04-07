from os import path
from samri.pipelines import glm

scratch_dir = '~/.scratch/opfvta'

preprocess_base = path.join(scratch_dir,'preprocess')

glm.l1(preprocess_base,
	bf_path='../data/chr_beta1.txt',
	habituation=None,
	mask='mouse',
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'modality':['cbv']},
	invert=True,
	workflow_name='l1',
	out_base=scratch_dir,
	)

glm.seed(preprocess_base,'../data/vta_right.nii.gz',
	mask='mouse',
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={
		'modality':['cbv'],
		},
	lowpass_sigma=2,
	highpass_sigma=225,
	out_base=scratch_dir,
	workflow_name='seed_l1',
	metric='median',
	top_voxel='{}/l1/sub-{{subject}}/ses-{{session}}/sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_desc-tstat_{{modality}}.nii.gz'.format(scratch_dir),
	)

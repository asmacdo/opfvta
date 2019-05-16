from os import path
from samri.pipelines import glm

scratch_dir = '~/.scratch/opfvta'

preprocess_base = path.join(scratch_dir,'preprocess')

glm.l1(preprocess_base,
	convolution='dgamma',
	habituation='in_main_contrast',
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_DGmainhab',
	out_base=scratch_dir,
	)
glm.l1(preprocess_base,
	convolution='dgamma',
	habituation=False,
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_DGnohab',
	out_base=scratch_dir,
	)

glm.l1(preprocess_base,
	convolution='gamma',
	habituation='in_main_contrast',
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_Gmainhab',
	out_base=scratch_dir,
	)
glm.l1(preprocess_base,
	convolution='gamma',
	habituation=False,
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_Gnohab',
	out_base=scratch_dir,
	)

glm.l1(preprocess_base,
	bf_path='../data/chr_beta1.txt',
	habituation='in_main_contrast',
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_Cmainhab',
	out_base=scratch_dir,
	)
glm.l1(preprocess_base,
	bf_path='../data/chr_beta1.txt',
	habituation=None,
	mask='mouse',
	#keep_work=True,
	n_jobs_percentage=.33,
	exclude={
		'task':['rest','JPogT'],
		},
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1_Cnohab',
	out_base=scratch_dir,
	)

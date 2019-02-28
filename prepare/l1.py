from os import path
from samri.pipelines import glm

scratch_dir = '~/.scratch/opfvta'

preprocess_base = path.join(scratch_dir,'preprocess')

glm.l1(preprocess_base,
	bf_path='../data/chr_beta1.txt',
	habituation='in_main_contrast',
	mask='mouse',
	keep_work=False,
	n_jobs_percentage=.33,
	match={'type':['cbv']},
	invert=True,
	workflow_name='l1',
	out_base=scratch_dir,
	)

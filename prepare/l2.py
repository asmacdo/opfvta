from os import path
from samri.pipelines import glm

scratch_dir = '~/data_scratch/opfvta'
l1_base = '{}/l1/'.format(scratch_dir)

glm.l2_common_effect(l1_base,
	workflow_name='omnibus',
	mask='/home/hioanas/gentoo/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	groupby='task',
	keep_work=True,
	n_jobs_percentage=.33,
	#include={'run':['1'],},
	out_base='{}/l2'.format(scratch_dir),
	)

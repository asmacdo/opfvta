from os import path

from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations

scratch_dir = '~/.scratch/opfvta'
bids_base = path.join(scratch_dir,'bids')

# Preprocess all of the data:
generic(bids_base,
	#functional_blur_xy=0.4,
	template='mouse',
	functional_match={'acquisition':['EPI'],},
	structural_match={'acquisition':['TurboRARE'],},
        workflow_name='preprocess',
	out_base=scratch_dir,
	)

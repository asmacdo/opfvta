from os import path

from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations

scratch_dir = '~/data_scratch/opfvta'
bids_base = path.join(scratch_dir,'bids')

# Preprocess all of the data:
generic(bids_base,
	template='mouse',
	functional_match={'acquisition':['EPI'],},
	structural_match={'acquisition':['TurboRARE'],},
	actual_size=True,
        workflow_name='preprocess',
	out_base=scratch_dir,
	)

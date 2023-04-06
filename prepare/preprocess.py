import pandas as pd
from os import path

from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations

scratch_dir = '~/.scratch/opfvta'
bids_base = path.join(scratch_dir,'bids')

groups_path = path.abspath('../data/groups.csv')
groups = pd.read_csv(groups_path)
groups = groups.loc[groups['OrthogonalStereotacticTarget_depth'].notnull()]
subjects = list(groups.Subject.unique())

# Preprocess all of the data:
generic(bids_base,
	functional_blur_xy=0.25,
	template='mouse',
	subjects=subjects,
	functional_match={'acquisition':['EPI'],},
	structural_match={'acquisition':['TurboRARE'],},
        workflow_name='preprocess',
	out_base=scratch_dir,
	n_jobs_percentage=0.75,
	)

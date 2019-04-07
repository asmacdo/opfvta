import pandas as pd
from samri.pipelines.reposit import bru2bids

import numpy as np

df = pd.read_csv('../data/groups.csv')
ids = sorted(df['subject'].tolist())

data_dir = '~/ni_data/ofM.vta'
bru2bids(data_dir,
	inflated_size=False,
	functional_match={
		"subject":ids,
		'acquisition':['EPI'],
		},
	structural_match={
		"subject":ids,
		'acquisition':['TurboRARE'],
		},
	out_base='~/.scratch/opfvta',
	keep_crashdump=True,
	)

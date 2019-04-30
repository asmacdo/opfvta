import os
import pandas as pd
from samri.pipelines.reposit import bru2bids
from labbookdb.report.selection import animal_id, parameterized
from datetime import datetime

df = pd.read_csv('../data/groups.csv')
ids = sorted(df['Subject'].tolist())

db_path = '~/syncdata/meta.db'
data_dir = '~/ni_data/ofM.vta'
base_dir = '~/.scratch/opfvta'
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
	out_base=base_dir,
	keep_crashdump=True,
	)

# Add irregularity metadata
subjects = [animal_id(db_path, 'ETH/AIC', i) for i in ids]

irregularities = parameterized(db_path,'animals measurements irregularities',animal_filter=subjects)

bids_dir = os.path.expanduser('{}/bids'.format(base_dir))
for sub_dir in os.listdir(bids_dir):
	sub_path = os.path.join(bids_dir,sub_dir)
	if os.path.isdir(sub_path) and sub_dir[:4] == 'sub-':
		sessions_file = os.path.join(sub_path,'{}_sessions.tsv'.format(sub_dir))
		if os.path.isfile(sessions_file):
			sessions = pd.read_csv(sessions_file, sep='\t')
			sessions['irregularities']=''
			for mydate in sessions['acq_time'].unique():
				mydate_date = datetime.strptime(mydate,'%Y-%m-%dT%H:%M:%S')
				irregularity_list = irregularities.loc[irregularities['Measurement_date']==mydate_date,'Irregularity_description'].tolist()
				irregularity_list = '; '.join(irregularity_list)
				sessions.loc[sessions['acq_time']==mydate,'irregularities'] = irregularity_list
			sessions.to_csv(sessions_file, sep='\t', index=False)

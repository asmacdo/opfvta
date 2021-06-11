import pandas as pd
from os import path

data_path = path.abspath(path.expanduser('data/participants.tsv'))
try:
	df = pd.read_csv(data_path, sep='\t')
except FileNotFoundError:
	data_path = '/usr/share/opfvta_bidsdata/participants.tsv'
	df = pd.read_csv(data_path, sep='\t')

m = len(df.loc[(df['sex']=='m', 'participant_id')].unique())
f = len(df.loc[(df['sex']=='f', 'participant_id')].unique())
print('{} males and {} females'.format(m,f))

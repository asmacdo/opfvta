import pandas as pd
from os import path

data_path = path.abspath(path.expanduser('~/.scratch/opfvta/bids/participants.tsv'))
try:
	df = pd.read_csv(data_path, sep='\t')
except FileNotFoundError:
	data_path = '/usr/share/opfvta_bidsdata/participants.tsv'
	df = pd.read_csv(data_path, sep='\t')

m = len(df.loc[(df['sex']=='m')])
f = len(df.loc[(df['sex']=='f')])
print('{} males and {} females'.format(m,f))

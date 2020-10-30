from labbookdb.report.tracking import append_external_identifiers
from labbookdb.report.selection import animal_id, animals_by_genotype, animal_operations, parameterized
import pandas as pd
from os import path
import numpy as np

db_path='~/syncdata/meta.db'

participants_path = path.abspath(path.expanduser('~/.scratch/opfvta/bids/participants.tsv'))
try:
        participants_df = pd.read_csv(participants_path, sep='\t')
except FileNotFoundError:
        participants_path = '/usr/share/opfvta_bidsdata/participants.tsv'
        participants_df = pd.read_csv(participants_path, sep='\t')
ids = [str(i) for i in participants_df['subject'].unique()]
ids = [animal_id(db_path, 'ETH/AIC',i) for i in ids]

df = animals_by_genotype(db_path, ['datg','dawt'])
df = df.rename(columns={'Animal_id':'Subject'})
df['Subject'] = df['Subject'].apply(lambda x: animal_id(db_path,'ETH/AIC',str(x),reverse=True))
df = df.drop(['Genotype_id'], axis=1)

_operations = animal_operations(db_path, animal_ids=ids)
operations = pd.DataFrame([])
for i in _operations['Animal_id'].unique():
	df_ = _operations.loc[_operations['Animal_id']==i]
	df_ = df_.drop(['Operation_id','Operation_operator_id','Operation_anesthesia_id'], 1)
	if len(df_) == 1:
		df_['Operation_delay'] = 0
		operations = pd.concat([operations,df_],sort=True)
	else:
		a,b = df_['Operation_date'].unique()
		delay = (b-a)/np.timedelta64(1, 'D')
		delay = round(int(delay))
		df_ = df_.groupby('Animal_id').transform(lambda x: x.bfill().ffill())
		df_['Animal_id'] = i
		df_['Operation_date'] = df_['Operation_date'].tolist()[0]
		df_ = df_.drop_duplicates()
		df_['Operation_delay'] = delay
		operations = pd.concat([operations,df_],sort=True)

operations['PA rel. Bregma [mm]'] = operations['OrthogonalStereotacticTarget_posteroanterior']
operations['Depth rel. skull [mm]'] = operations['OrthogonalStereotacticTarget_depth']
operations['\Delta PA_{Bregma}'] = operations['OrthogonalStereotacticTarget_posteroanterior']
# Removing internal LabbookDB identifier columns
operations = operations.drop(
	[
		'Operation_animal_id',
		'OpticFiberImplantProtocol_code',
		'OpticFiberImplantProtocol_id',
		'OpticFiberImplantProtocol_name',
		'OpticFiberImplantProtocol_optic_fiber_implant_id',
		'OpticFiberImplantProtocol_stereotactic_target_id',
	],
	axis=1,
	)

operations = operations.rename(columns={'Animal_id':'Subject'})
operations['Subject'] = operations['Subject'].apply(lambda x: animal_id(db_path, 'ETH/AIC', x, reverse=True))
df = pd.merge(df, operations, on='Subject', how='inner')
df = df.loc[df['Subject']!='FailedIDQuery']
df.to_csv('../data/groups.csv')

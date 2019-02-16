from labbookdb.report.selection import animal_id, animal_operations, parameterized
import pandas as pd
from os import path
import numpy as np

db_path='~/syncdata/meta.db'
data_path = path.abspath('../data/functional_significance.csv')
df = pd.read_csv(data_path)

subjects = df['Subject'].unique()
ids = [animal_id(db_path, 'ETH/AIC', str(i)) for i in subjects]
genotypes = parameterized(db_path, 'animals info', animal_filter=ids)
genotypes = genotypes.loc[genotypes['AnimalExternalIdentifier_database']=='ETH/AIC']

_operations = animal_operations(db_path, animal_ids=ids)
operations = pd.DataFrame([])
for i in _operations['Animal_id'].unique():
	df = _operations.loc[_operations['Animal_id']==i]
	df = df.drop(['Operation_id','Operation_operator_id','Operation_anesthesia_id'], 1)
	if len(df) == 1:
		df['Operation_delay'] = 0
		operations = pd.concat([operations,df],sort=True)
	else:
		a,b = df['Operation_date'].unique()
		delay = (b-a)/np.timedelta64(1, 'D')
		delay = round(int(delay))
		df = df.groupby('Animal_id').transform(lambda x: x.bfill().ffill())
		df['Animal_id'] = i
		df['Operation_date'] = df['Operation_date'].tolist()[0]
		df = df.drop_duplicates()
		df['Operation_delay'] = delay
		operations = pd.concat([operations,df],sort=True)

operations['PA rel. Bregma [mm]'] = operations['OrthogonalStereotacticTarget_posteroanterior']
operations['Depth rel. skull [mm]'] = operations['OrthogonalStereotacticTarget_depth']
operations['\Delta PA_{Bregma}'] = operations['OrthogonalStereotacticTarget_posteroanterior']
# Removing internal LabbookDB identifier columns
df = df.drop(
	[
		'Operation_animal_id',
		'OpticFiberImplantProtocol_code',
		'OpticFiberImplantProtocol_id',
		'OpticFiberImplantProtocol_name',
		'OpticFiberImplantProtocol_optic_fiber_implant_id',
		'OpticFiberImplantProtocol_stereotactic_target_id',
	],
	1)

operations['Subject'] = operations['Animal_id'].apply(lambda x: animal_id(db_path, 'ETH/AIC', x, reverse=True))
operations.to_csv('../data/groups.csv')

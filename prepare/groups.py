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

operations = animal_operations(db_path, animal_ids=ids)
_operations = pd.DataFrame([])
for i in operations['Animal_id'].unique():
	df = operations.loc[operations['Animal_id']==i]
	df = df.drop(['Operation_id','Operation_operator_id','Operation_anesthesia_id'], 1)
	if len(df) == 1:
		df['Operation_delay'] = 0
		_operations = pd.concat([_operations,df],sort=True)
	else:
		a,b = df['Operation_date'].unique()
		delay = (b-a)/np.timedelta64(1, 'D')
		delay = round(int(delay))
		df = df.groupby('Animal_id').transform(lambda x: x.bfill().ffill())
		df['Animal_id'] = i
		df['Operation_delay'] = delay
		_operations = pd.concat([_operations,df],sort=True)

#print(ids)
#print(genotypes['AnimalExternalIdentifier_animal_id'])
#print(operations['Animal_id'])
_operations.to_csv('_operations.csv')
#print(len(operations))
#print(len(genotypes))
#print(operations[['OrthogonalStereotacticTarget_code','Virus_OrthogonalStereotacticTarget_code']])

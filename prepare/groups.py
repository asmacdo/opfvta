from labbookdb.report.selection import animal_id, animal_operations, parameterized
import pandas as pd
from os import path

db_path='~/syncdata/meta.db'
data_path = path.abspath('../data/functional_significance.csv')
df = pd.read_csv(data_path)

subjects = df['Subject'].unique()
ids = [animal_id(db_path, 'ETH/AIC', str(i)) for i in subjects]
genotypes = parameterized(db_path, 'animals info', animal_filter=ids)
operations = animal_operations(db_path, animal_ids=ids)

print(ids)
print(genotypes['Genotype_code'])
print(operations)
print(operations[['OrthogonalStereotacticTarget_code','Virus_OrthogonalStereotacticTarget_code']])

from labbookdb.report.tracking import append_external_identifiers
from labbookdb.report.selection import animals_by_genotype

db_path='~/syncdata/meta.db'

df = animals_by_genotype(db_path, ['dawt','datg'])
df = append_external_identifiers(db_path, df)
df = df.drop(['Animal_id','UZH/iRATS','Genotype_id'], axis=1)
df.to_csv('../data/groups.csv')

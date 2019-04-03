from labbookdb.report.tracking import append_external_identifiers
from labbookdb.report.selection import animal_id, animals_by_genotype

db_path='~/syncdata/meta.db'

df = animals_by_genotype(db_path, ['datg','dawt'])
df = df.rename(columns={'Animal_id':'subject'})
df['subject'] = df['subject'].apply(lambda x: animal_id('~/syncdata/meta.db','ETH/AIC',str(x),reverse=True))
df = df.drop(['Genotype_id'], axis=1)
df = df.loc[df['subject']!='FailedIDQuery']
df.to_csv('../data/groups.csv')

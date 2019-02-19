import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from os import path
from lib.utils import float_to_tex, inline_anova, inline_factor

#def factorci(factor,
#	df_path='data/volumes.csv',
#	dependent_variable='Volume Change Factor',
#	expression='Processing*Template',
#	exclusion_criteria={},
#	**kwargs
#	):

df_path = path.abspath('../data/functional_t.csv')
groups_path = path.abspath('../data/groups.csv')
df = pd.read_csv(df_path)
groups = pd.read_csv(groups_path)

df = pd.merge(df, groups, on='Subject', how='outer')
#df = df.loc[pd.notnull(df['Depth rel. skull [mm]']) & pd.notnull(df['PA rel. Bregma [mm]'])]
df = df.dropna(subset=['Depth rel. skull [mm]', 'PA rel. Bregma [mm]'])

print(df.columns)
#print(df)
#print(groups)
#df.to_csv('df.csv')

formula = 'Q("Mean VTA t") ~ Q("Depth rel. skull [mm]") + Q("PA rel. Bregma [mm]") + Task'
model = smf.mixedlm(formula, df, groups='Subject')
fit = model.fit()
summary = fit.summary()
print(summary)
#tex = inline_factor(summary, factor, 'tex', **kwargs)

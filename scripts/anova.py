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

df_path = path.abspath('../data/functional_significance.csv')
groups_path = path.abspath('../data/groups.csv')
df = pd.read_csv(df_path)
groups = pd.read_csv(groups_path)

print(df)
print(groups)

#formula = 'Q("{}") ~ {}'
#model = smf.mixedlm(formula, df, groups='Uid')
#fit = model.fit()
#summary = fit.summary()
#tex = inline_factor(summary, factor, 'tex', **kwargs)

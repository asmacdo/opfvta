import numpy as np
import os
import pandas as pd
import portage

from samri.report.snr import df_significant_signal, df_roi_data
from samri.utilities import bids_autofind_df

prefix = portage.root
scratch_dir = os.path.expanduser('~/.scratch/opfvta/')

task_categories = {
	'CogBl':'Block',
	'CogBr':'Block',
	'CogBm':'Block',
	'CogMwf':'Block',
	'CogB':'Block',
	'JPogP':'Phasic',
	'CogP':'Phasic',
	#'JPogT':'Tonic',
	}

# Total significance
habituations = [
        i[3:]
        for i in os.listdir(scratch_dir)
        if i.startswith('l1_') and not i.endswith('_work')
        ]

df = pd.DataFrame([])
for h in habituations:
	in_df = bids_autofind_df('{}/l1_{}/'.format(scratch_dir,h),
		path_template='sub-{{subject}}/ses-{{session}}/'\
			'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_{{modality}}_pfstat.nii.gz',
		match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/'\
			'.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_(?P<modality>cbv|bold)_pfstat\.nii\.gz',
		)
	df_ = df_significant_signal(in_df,
		mask_path='{}/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'.format(prefix),
		exclude_ones=True,
		)
	df_ = df_significant_signal(df_,
		mask_path='../data/vta_right.nii.gz',
		column_string='VTA Significance',
		exclude_ones=True,
		)
	df_['habituation'] = h
	df = df.append(df_)

# Ready Strings for Printing
df['modality'] = df['modality'].str.upper()
df.columns = map(str.title, df.columns)
df = df.rename(
	columns={
		'Mean Vta Significance':'Mean VTA Significance',
		'Median Vta Significance':'Median VTA Significance',
		'Modality':'Contrast',
		})

df['Task Category'] = df['Task']
df = df.replace({'Task Category': task_categories})

df.to_csv('../data/functional_significance_all.csv')
df = df.loc[df['Habituation']=='DGnohab']
df.to_csv('../data/functional_significance.csv')

# VTA Significance

# Total significance
habituations = [
        i[3:]
        for i in os.listdir(scratch_dir)
        if i.startswith('l1_') and not i.endswith('_work')
        ]

df = pd.DataFrame([])
for h in habituations:
	in_df = bids_autofind_df('{}/l1_{}/'.format(scratch_dir,h),
		path_template='sub-{{subject}}/ses-{{session}}/'\
			'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_{{modality}}_tstat.nii.gz',
		match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/'\
			'.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_(?P<modality>cbv|bold)_tstat\.nii.gz',
		)
	df_ = df_roi_data(in_df,
		mask_path='../data/vta_right.nii.gz',
		column_string='VTA t',
		)
	df_['habituation'] = h
	df = df.append(df_)

# Ready Strings for Printing
df['modality'] = df['modality'].str.upper()
df.columns = map(str.title, df.columns)
df = df.rename(
	columns={
		'Mean Vta T':'Mean VTA t',
		'Median Vta T':'Median VTA t',
		'Modality':'Contrast',
		})

# Create processing and template-independent unique identifiers
df['Scan'] = df['Subject']+':'+df['Session']+':'+df['Contrast']

df['Task Category'] = df['Task']
df = df.replace({'Task Category': task_categories})

# Stimulation protocol parametrization
df['Frequencies'] = ''
df['Frequency'] = ''
df['Durations'] = ''
df['Duration'] = ''
df['Pulse Width'] = ''
df['Pulse Widths'] = ''
for task in df['Task'].unique():
	events = pd.read_csv('../data/{}.tsv'.format(task), sep='\t')
	df.loc[df['Task']==task, 'Frequencies'] = ','.join([str(i) for i in events['frequency'].unique()])
	df.loc[df['Task']==task, 'Frequency'] = np.mean(events['frequency'].unique())
	df.loc[df['Task']==task, 'Durations'] = ','.join([str(i) for i in events['duration'].unique()])
	df.loc[df['Task']==task, 'Duration'] = np.mean(events['duration'].unique())
	df.loc[df['Task']==task, 'Pulse Widths'] = ','.join([str(i) for i in events['pulse_width'].unique()])
	df.loc[df['Task']==task, 'Pulse Width'] = np.mean(events['pulse_width'].unique())

df.to_csv('../data/functional_t_all.csv')
df = df.loc[df['Habituation']=='DGnohab']
df.to_csv('../data/functional_t.csv')

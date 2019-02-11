import pandas as pd

from samri.report.snr import df_significant_signal
from samri.report.utilities import df_roi_data
from samri.utilities import bids_autofind_df

scratch_dir = '~/data_scratch/opfvta/'

# Total significance

df = pd.DataFrame([])
in_df = bids_autofind_df('{}/l1/'.format(scratch_dir),
	path_template='sub-{{subject}}/ses-{{session}}/'\
		'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_{{modality}}_pfstat.nii.gz',
	match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/'\
		'.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_(?P<modality>cbv|bold)_pfstat\.nii\.gz',
	)
df_ = df_significant_signal(in_df,
	mask_path='/home/hioanas/gentoo/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	exclude_ones=True,
	)
df_ = df_significant_signal(df_,
	mask_path='../data/vta.nii.gz',
	column_string='VTA Significance',
	exclude_ones=True,
	)
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

df.to_csv('../data/functional_significance.csv')

df = pd.DataFrame([])
in_df = bids_autofind_df('{}/l1/'.format(scratch_dir),
	path_template='sub-{{subject}}/ses-{{session}}/'\
		'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_{{modality}}_tstat.nii.gz',
	match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/'\
		'.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_(?P<modality>cbv|bold)_tstat\.nii.gz',
	)
df_ = df_roi_data(in_df,
	mask_path='../data/vta.nii.gz',
	column_string='VTA t',
	)
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

df.to_csv('../data/functional_t.csv')

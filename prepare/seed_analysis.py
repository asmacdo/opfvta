from os import path
from samri.utilities import bids_autofind
from samri.analysis import fc

scratch_dir = path.abspath(path.expanduser('~/.scratch'))
scratch_dir = path.join(scratch_dir,'opfvta')

template , substitutions = bids_autofind('{}/preprocess/'.format(scratch_dir),
        path_template='sub-{{subject}}/ses-{{session}}/func/'\
                'sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_cbv.nii.gz',
        match_regex='.+sub-(?P<sub>.+)/ses-(?P<ses>.+)/func/'\
                '.*?_task-(?P<task>.+)_acq-(?P<acquisition>.+)_run-(?P<run>.+)_cbv\.nii\.gz',
        )

fc_results = fc.seed_based(substitutions, '/usr/share/mouse-brain-atlases/dsurqec_200micron_roi-dr.nii', '/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	ts_file_template=template,
	save_results='{}/fc/sub-{{subject}}/ses-{{session}}/sub-{{subject}}_ses-{{session}}_task-{{task}}_acq-{{acquisition}}_run-{{run}}_cbv.nii.gz'.format(scratch_dir),
	)

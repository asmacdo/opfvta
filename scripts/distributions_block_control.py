from samri.plotting.aggregate import roi_distributions
from samri.report.roi import atlasassignment

df = atlasassignment('data/seed_l2/alias-block_control/acq-EPI_tstat.nii.gz',
        lateralized=True,
        value_label='t Values',
        )

df['Structure'] = df['Structure'].str.title()
roi_distributions(df,
        max_rois=10,
        exclude_tissue_type=['CSF'],
        #xlim=[-3,6],
        start=0.3,
        cmap='autumn_r',
        value_label='t Values',
        bw=.1,
        hspace=-0.5,
        )
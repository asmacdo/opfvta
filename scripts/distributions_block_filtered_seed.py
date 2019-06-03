from samri.plotting.aggregate import roi_distributions
from samri.report.roi import atlasassignment
import matplotlib.pyplot as plt

df = atlasassignment('data/seed_l2/alias-block_filtered/acq-EPI_tstat.nii.gz',
        lateralized=True,
        value_label='t Values',
        )

df['Structure'] = df['Structure'].str.title()
roi_distributions(df,
        max_rois=10,
        exclude_tissue_type=['CSF'],
        #xlim=[-19,10],
        start=0.3,
        cmap='autumn_r',
        value_label='t Values',
        bw=.1,
        )

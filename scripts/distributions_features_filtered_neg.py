from samri.plotting.aggregate import roi_distributions
from samri.report.roi import atlasassignment
import matplotlib.pyplot as plt

stat_map = "data/features_l2/_tstat.nii.gz"

df = atlasassignment(stat_map,
        lateralized=True,
        value_label='t Values',
        )

df['Structure'] = df['Structure'].str.title()
roi_distributions(df,
        ascending=True,
        max_rois=10,
        exclude_tissue_type=['CSF'],
        xlim=[-6.3,2.7],
        start=0.3,
        cmap='viridis_r',
        value_label='t Values',
        bw=.1,
        #text_side='right',
        hspace=-0.5,
        )

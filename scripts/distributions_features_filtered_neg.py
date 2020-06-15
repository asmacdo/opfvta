from samri.plotting.aggregate import roi_distributions
from samri.report.roi import atlasassignment
import matplotlib.pyplot as plt

stat_map = "data/features_l2/_tstat.nii.gz"

df = atlasassignment(stat_map,
        lateralized=True,
        value_label='t Values',
        )
df['Structure'] = df['Structure'].replace({
        'Accessory olfactory bulb: glomerular, external plexiform and mitral cell layer': 'Accessory olfactory bulb: glomerular, external plexiform, mitral layers',
        })
df['Structure'] = df['Structure'].str.title()
df['Structure'] = df['Structure'].replace({
        'Anterior':'Ant.',
        'Endopiriform Claustrum':'EC',
        'Intermediate':'Int.',
        'Medial':'Med.',
        'Nucleus':'Nc.',
        'Pars':'p.',
        'Posterior':'Post.',
        'White Matter':'WM',
        },
        regex=True,
        )

roi_distributions(df,
        ascending=True,
        max_rois=10,
        exclude_tissue_type=['CSF'],
        xlim=[-5,2.7],
        start=0.3,
        cmap='summer_r',
        value_label='t Values',
        bw=.1,
        text_side='right',
        hspace=-0.5,
        )

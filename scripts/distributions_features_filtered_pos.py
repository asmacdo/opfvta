from samri.plotting.aggregate import roi_distributions
from samri.report.roi import atlasassignment
import matplotlib.pyplot as plt

stat_map = "data/features_l2/_tstat.nii.gz"

df = atlasassignment(stat_map,
        lateralized=True,
        value_label='t Values',
        )
#print(df.loc[df['Structure'] == 'Accessory olfactory bulb: glomerular, external plexiform and mitral cell layer'])
#print(df.loc[df['Structure'] == 'Accessory olfactory bulb: glomerular, external plexiform and mitral cell layer'])
#df = df.replace('Accessory olfactory bulb: glomerular, external plexiform and mitral cell layer','Accessory olfactory bulb: glomerular, external plexiform, mitral layers')

df['Structure'] = df['Structure'].str.title()
roi_distributions(df,
        max_rois=10,
        exclude_tissue_type=['CSF'],
        xlim=[-2.5,6.2],
        start=0.3,
        cmap='plasma_r',
        value_label='t Values',
        bw=.1,
        hspace=-0.5,
        )

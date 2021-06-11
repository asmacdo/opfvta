import samri.plotting.maps as maps
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

COLORS_PLUS = plt.cm.spring(np.linspace(0., 1, 128))
COLORS_MINUS = plt.cm.summer(np.linspace(0, 1, 128))
COLORS = np.vstack((COLORS_MINUS, COLORS_PLUS[::-1]))
MYMAP = mcolors.LinearSegmentedColormap.from_list('my_colormap', COLORS)

scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/features_l2/_tstat.nii.gz"
template = "/usr/share/mouse-brain-templates/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	cmap=MYMAP,
	cut_coords=(0.55,-3.45,-4.8),
	)

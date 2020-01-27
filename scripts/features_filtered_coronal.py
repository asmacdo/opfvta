import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import samri.plotting.maps as maps

COLORS_PLUS = plt.cm.plasma(np.linspace(0., 1, 128))
COLORS_MINUS = plt.cm.viridis(np.linspace(0, 1, 128))
COLORS = np.vstack((COLORS_MINUS, COLORS_PLUS[::-1]))
MYMAP = mcolors.LinearSegmentedColormap.from_list('my_colormap', COLORS)

#heatmap_image = 'data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz'
heatmap_image = "data/features_l2/_tstat.nii.gz"
#contour_image = 'data/vta_projection_tstat.nii.gz'

maps.slices(heatmap_image,
	ratio=7/5.,
	auto_figsize=False,
	style=False,
	position_vspace=0,
	slice_spacing=0.45,
	cmap=MYMAP,
	skip_start=2,
	skip_end=2,
	)

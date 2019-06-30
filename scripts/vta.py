import samri.plotting.maps as maps
from samri.fetch.local import roi_from_atlaslabel

stat_map = "data/vta_right.nii.gz"
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	scale=0.3,
	alpha=0.75,
	template=template,
	show_plot=False,
	threshold=0.8,
	threshold_mesh=0.8,
	draw_colorbar=False,
	cmap=['#ff6600'],
	)

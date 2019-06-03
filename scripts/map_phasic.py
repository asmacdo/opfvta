import samri.plotting.maps as maps

stat_map = "data/l2/alias-phasic/acq-EPI_tstat.nii.gz"
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	cut_coords=(0.5,-3.2,-4.5),
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	)

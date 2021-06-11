import samri.plotting.maps as maps

stat_map = "data/l2/alias-block/acq-EPI_tstat.nii.gz"
template = "/usr/share/mouse-brain-templates/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	)

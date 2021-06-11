import samri.plotting.maps as maps

scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/seed_l2/alias-block_filtered/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-templates/dsurqec_40micron_masked.nii"
seed = "data/vta_right.nii.gz"

maps.stat3D(stat_map,
	overlays=[seed],
	cut_coords=(0.55,-3.45,-4.8),
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	positive_only=True,
	contour_colors=['#22dd22'],
	)

import samri.plotting.maps as maps
scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/l2/alias-block_other/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-templates/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	template=template,
	scale=0.3,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	)

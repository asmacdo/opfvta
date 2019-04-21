import samri.plotting.maps as maps

scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/l2/alias-phasic_other/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	cut_coords=(0.5,-3.2,-4.5),
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=2,
	threshold_mesh=2,
	)

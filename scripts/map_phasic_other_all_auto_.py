import samri.plotting.maps as maps
scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/l2_/alias-phasic_other/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	template=template,
	scale=0.3,
	show_plot=False,
	threshold=2,
	threshold_mesh=2,
	)

import samri.plotting.maps as maps

scratch_dir = '~/.scratch/opfvta/'

stat_map = "data/l2/sub-6573.6574.6575.6576.6578.6586.6587.6588.6589.6590.6591.6592.6593.3839.6639.6643.6642/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	cut_coords=(0.5,-3.2,-4.5),
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	)

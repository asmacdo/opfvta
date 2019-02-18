import samri.plotting.maps as maps

scratch_dir = '~/data_scratch/opfvta/'

stat_map = "{}/l2/sub-6257.6259.6260.5681.5682.5683.5685.6467.6468/acq-EPI_tstat.nii.gz".format(scratch_dir)
template = "/usr/share/mouse-brain-atlases/dsurqec_40micron_masked.nii"

maps.stat3D(stat_map,
	cut_coords=[(0.5,-3.2,-4.5)],
	scale=0.3,
	template=template,
	show_plot=False,
	threshold=3,
	threshold_mesh=3,
	)

import samri.plotting.maps as maps

heatmap_image = 'data/l2/alias-block_other_controlled/acq-EPI_tstat.nii.gz'
contour_image = 'data/vta_projection_tstat.nii.gz'

maps.slices(heatmap_image,
	contour_image=contour_image,
	auto_figsize=False,
	)

import samri.plotting.maps as maps

heatmap_image = 'data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz'
contour_image = 'data/vta_projection_tstat.nii.gz'

maps.slices(heatmap_image,
	contour_image=contour_image,
	ratio=7/5.,
	auto_figsize=False,
	style=False,
	position_vspace=0.1,
	positive_only=True,
	skip_start=1,
	slice_spacing=0.45,
	)

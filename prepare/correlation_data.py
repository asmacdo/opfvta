import json
import numpy as np
from samri.report.utilities import voxels_for_comparison, rois_for_comparison

img1 = '../data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz'
img2 = '../data/vta_projection_tstat.nii.gz'

correlation_data = {}

img1_voxels, img2_voxels = voxels_for_comparison(img1, img2,
	mask_path='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
	resample_voxel_size=[0.225,0.45,0.225],
	)
correlation_data['voxelwise'] = {}
correlation_data['voxelwise']['functional'] = [str(i) for i in list(img1_voxels)]
correlation_data['voxelwise']['structural'] = [str(i) for i in list(img2_voxels)]

img1_rois, img2_rois, roi_names = rois_for_comparison(img1, img2)

correlation_data['regionwise'] = {}
correlation_data['regionwise']['functional'] = [str(i) for i in list(img1_rois)]
correlation_data['regionwise']['structural'] = [str(i) for i in list(img2_rois)]
correlation_data['regionwise']['ROIs'] = [str(i) for i in list(roi_names)]

with open('../data/correlation_data.json', 'w') as outfile:
    json.dump(correlation_data, outfile)

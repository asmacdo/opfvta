import json
from scipy import stats
from lib.utils import float_to_tex

with open('data/correlation_data.json') as json_file:
	correlation_data = json.load(json_file)

img1_voxels = [float(i) for i in correlation_data['voxelwise']['functional']]
img2_voxels = [float(i) for i in correlation_data['voxelwise']['structural']]
img1_rois = [float(i) for i in correlation_data['regionwise']['functional']]
img2_rois = [float(i) for i in correlation_data['regionwise']['structural']]

r_voxels, p_voxels = stats.pearsonr(img1_voxels, img2_voxels)

r_rois, p_rois = stats.pearsonr(img1_rois, img2_rois)

r_voxels_tex = float_to_tex(r_voxels)
p_voxels_tex = float_to_tex(p_voxels)
r_rois_tex = float_to_tex(r_rois)
p_rois_tex = float_to_tex(p_rois)

latex = ', with a parcellation region based correlation of {rr} ({pr}), and a voxel-wise correlation of {rv} ({pv})'.format(
	rr=r_rois_tex,
	pr=p_rois_tex,
	rv=r_voxels_tex,
	pv=p_voxels_tex,
	)

print(latex)

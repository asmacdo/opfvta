from samri.pipelines.preprocess import generic, legacy
from samri.pipelines import manipulations

bids_base = '~/ni_data/ofM.vta/bids'

# Preprocess all of the data:
generic(bids_base, "/usr/share/mouse-brain-atlases/dsurqec_200micron.nii",
	registration_mask="/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii",
	functional_match={'acquisition':['EPI'],},
	structural_match={'acquisition':['TurboRARE'],},
	actual_size=True,
	out_base='~/ni_data/ofM.vta/preprocessing',
	)

from samri.pipelines.reposit import bru2bids

data_dir = '~/ni_data/ofM.vta'

bru2bids(data_dir,
	inflated_size=False,
	functional_match={'acquisition':['EPI']},
	structural_match={'acquisition':['TurboRARE','TurboRAREhd']},
	keep_work=True,
        keep_crashdump=True,
        )

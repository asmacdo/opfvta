from samri.pipelines.reposit import bru2bids

data_dir = '~/ni_data/ofM.vta'

bru2bids(data_dir,
	inflated_size=False,
	functional_match={
		'acquisition':['EPI'],
		#'subject':['6590','6591','6643','6639','6593','6642'],
		},
	structural_match={
		'acquisition':['TurboRARE','TurboRAREhd'],
		#'subject':['6590','6591','6643','6639','6593','6642'],
		},
	#keep_work=True,
        keep_crashdump=True,
        )

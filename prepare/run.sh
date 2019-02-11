#!/usr/bin/env bash


if [ ! -d ~/data_scratch ]; then
	echo "You seem to be lacking a ~/data_scratch/ directory."
	echo "We need this directory in order to process the data, and it needs to be on a volume with 200GB+ space."
	echo "You can simply symlink to a location you would like this to happen (and then re-run this script):
		ln -s /where/you/want/it ~/data_scratch"
	exit 1
fi

if [ ! -d ~/data_scratch/opfvta/bids ]; then
	if [ -d "/usr/share/opfvta_bidsdata" ]; then
		[ -d ~/data_scratch/opfvta ] || mkdir ~/data_scratch/opfvta
		ln -s /usr/share/opfvta_bidsdata ~/data_scratch/opfvta/bids
	else
		echo "No OPFVTA BIDS data distribution found, processing from scanner OPFVTA data:"
		SAMRI bru2bids -o ~/data_scratch/opfvta/ -f '{"acquisition":["EPI"]}' -s '{"acquisition":["TurboRARE"]}' ~/ni_data/ofM.vta/
	fi
fi

python preprocess.py || exit 1
python l1.py || exit 1
python l2.py || exit 1
python functional_data.py || exit 1

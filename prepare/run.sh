#!/usr/bin/env bash
EXEC_PYTHON="python3"

# PREFIX=`$EXEC_PYTHON -c "import portage; print(portage.root)"`
PREFIX="/"

if [ ! -d ~/.scratch ]; then
	echo "You seem to be lacking a ~/.scratch/ directory."
	echo "We need this directory in order to process the data, and it needs to be on a volume with 200GB+ space."
	echo "You can simply symlink to a location you would like this to happen (and then re-run this script):
		ln -s /where/you/want/it ~/.scratch"
	exit 1
fi

if [ ! -d ~/.scratch/opfvta/bids ]; then
	if [ -d "/usr/share/opfvta_bidsdata" ]; then
		[ -d ~/.scratch/opfvta ] || mkdir ~/.scratch/opfvta
		ln -s "/usr/share/opfvta_bidsdata" ~/.scratch/opfvta/bids
	else
		echo "No OPFVTA BIDS data distribution found, processing from scanner OPFVTA data:"
		[ -d ~/.scratch/opfvta ] || mkdir ~/.scratch/opfvta
		$EXEC_PYTHON make_bids.py || exit 1
		$EXEC_PYTHON groups.py || exit 1
	fi
fi

if [ ! -d ~/.scratch/opfvta/preprocess ]; then
	$EXEC_PYTHON preprocess.py || exit 1
fi

$EXEC_PYTHON l1.py || exit 1
$EXEC_PYTHON features.py || exit 1
$EXEC_PYTHON functional_data.py || exit 1
$EXEC_PYTHON implant_coordinates.py || exit 1
$EXEC_PYTHON l2.py || exit 1
rsync -avP --exclude='*_cope.nii*' --exclude='*_zstat.nii*' ~/.scratch/opfvta/*l2* ../data/ || exit 1
$EXEC_PYTHON correlation_data.py

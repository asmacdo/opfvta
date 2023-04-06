#!/usr/bin/env bash

if [ ! -d ~/.local/share/data/opfvta_bidsdata ]; then
	mkdir -p ~/.local/share/data/opfvta_bidsdata
	pushd ~/.local/share/data/opfvta_bidsdata
	wget "https://zenodo.org/record/3575149/files/opfvta_bidsdata-2.0.tar.xz"
	tar xvf "opfvta_bidsdata-2.0.tar.xz"
	mv opfvta_bidsdata-2.0/* .
	rm opfvta_bidsdata*
fi

podman build . \
	-f Containerfile.partial \
	--name opfvta \
	-t opfvta-gentoo

# podman build . \
#       -f Containerfile \
#	--name opfvta \
#       -t opfvta-gentoo

podman run -it \
	-v ~/.local/share/data/opfvta_bidsdata:/usr/share/opfvta_bidsdata:Z \
	--detach \
	opfvta-gentoo /bin/bash

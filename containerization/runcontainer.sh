#!/usr/bin/env bash

# Downloading the data separately to bind mount into container
if [ ! -d ~/.local/share/data/opfvta_bidsdata ]; then
      mkdir -p ~/.local/share/data/opfvta_bidsdata
      pushd ~/.local/share/data/opfvta_bidsdata
	    wget "https://zenodo.org/record/3575149/files/opfvta_bidsdata-2.0.tar.xz"
	    tar xvf "opfvta_bidsdata-2.0.tar.xz"
	    mv opfvta_bidsdata-2.0/* .
	    rm opfvta_bidsdata*
      popd
fi

# Directory so that analysis traces are available on the host for inspection
mkdir -p ~/.local/share/data/opfvta_scratch

pushd ..
       # Running container with host-based directories bind mounted
       # Run an instance of the image
       podman run -it \
               -v ~/.local/share/data/opfvta_bidsdata:/usr/share/opfvta_bidsdata:Z \
               -v ~/.local/share/data/opfvta_scratch:/root/.scratch/:Z \
               --detach \
               --name opfvta-gentoo-instance-1 \
               opfvta-gentoo /bin/bash
popd


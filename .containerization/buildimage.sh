#!/usr/bin/env bash
pushd ..
       #podman build . \
       #       -f .containerization/Containerfile.partial \
       #       -t opfvta-gentoo
       podman build . \
               -f .containerization/Containerfile \
               -t opfvta-gentoo

popd

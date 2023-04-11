#!/usr/bin/env bash
pushd ..
       #podman build . \
       #       -f .containerization/Containerfile.partial \
       #       -t opfvta-gentoo
       podman build . \
              --no-cache \
               -f .containerization/Containerfile \
              -v ~/.local/cache/distfiles:/var/cache/distfiles \
               -t opfvta-distfiles-cached-gentoo

popd

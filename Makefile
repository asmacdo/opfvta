# TODO this should be disabled by default. We should
# Never assume the user wants to share any directory
# on their machine by default.
# DISTFILE_CACHE_PATH=~/.local/cache/distfiles

# Publishing variables
# Ideally these should be environment variables and we should check here whether they're defined and explain upload requires them if they're not.
SERVER=dreamarticles
WEBSITE=articles.chymera.eu
NAME=$(shell basename $(shell pwd))


# Set NOCLIENT variable to not prepend hostname to published filename:
# e.g. `NOCLIENT=1 make upload-article`
CLIENT := $(if $(NOCLIENT),$(shell cat /dev/null),$(shell hostname)_)

COMMON := bib.bib common_header.tex
PYTHONTEX_ALL := $(wildcard lib/* pythontex/* scripts/*)
STATIC_ALL := $(wildcard img/* *.sty)

all: article.pdf poster.pdf pitch.pdf slides.pdf

article.pdf:	$(wildcard article/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) article.tex
	rubber --pdf --unsafe article.tex
pitch.pdf:		$(wildcard pitch/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) pitch.tex
	rubber --pdf --unsafe pitch.tex
poster.pdf:	$(wildcard poster/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) poster.tex
	rubber --pdf --unsafe poster.tex
review.pdf:	$(wildcard poster/*) $(COMMON)
	rubber --pdf --unsafe review.tex
slides.pdf:		$(wildcard slides/*) $(COMMON) $(PYTHONTEX_ALL) $(STATIC_ALL) slides.tex
	rubber --pdf --unsafe slides.tex


# Cleanscripts
clean-article:
	rubber --clean article.tex
	rm _minted-article -rf
clean-pitch:
	rubber --clean pitch.tex
	rm _minted-pitch -rf
clean-poster:
	rubber --clean poster.tex
	rm _minted-poster -rf
clean-review:
	rubber --clean review.tex
	rm _minted-slides -rf
clean-slides:
	rubber --clean slides.tex
	rm _minted-slides -rf
clean: clean-article clean-pitch clean-poster clean-review clean-slides

# Upload scripts
upload: upload-article
upload-article: article.pdf
	rsync -avP article.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_article.pdf
upload-pitch: pitch.pdf
	rsync -avP pitch.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_pitch.pdf
upload-poster: poster.pdf
	rsync -avP poster.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_poster.pdf
upload-slides: slides.pdf
	rsync -avP slides.pdf ${SERVER}:${WEBSITE}/${CLIENT}${NAME}_slides.pdf



# Data preparation

data:	$(wildcard prepare/*)
	pushd prepare && ./run.sh


######## Containerized ########

# We must allow others exactly use our script without modification
# Or its not replicable by others.
#
REGISTRY ?= docker.io
REPOSITORY ?= asmacdo

IMAGE_NAME ?= opfvta
IMAGE_TAG ?= 2.0.0-alpha

FQDN_IMAGE=${REGISTRY}/${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}

build-fresh:
		# -v ${DISTFILE_CACHE_PATH}:/var/cache/distfiles
	podman build . \
		--no-cache \
		-f containerization/Containerfile \
		-t ${FQDN_IMAGE}

build-base:
		# -v ${DISTFILE_CACHE_PATH}:/var/cache/distfiles
	podman build . \
		-f containerization/Containerfile.base \
		-t opfvta-base

build:
		# -v ${DISTFILE_CACHE_PATH}:/var/cache/distfiles
	podman build . \
		-f containerization/Containerfile \
		-t ${FQDN_IMAGE}

push:
	podman push ${FQDN_IMAGE}

#		TODO(chymera) Folks using opfvta (from source or container) should not need to know the details of how to install SAMRI,
#		which requires mouse-brain-templates. Easiest fix is just to document in this README.
#
# FIXME(user): Users should use the following as an example, but requires preparation of 3 directories.
#		- Requires ../input_data/opfvta-bids (untar https://zenodo.org/record/3575149/files/opfvta_bidsdata-2.0.tar.xz)
#		- Requires ../reference_data/mouse-brain-templates-0.5.3 (untar http://chymera.eu/distfiles/mouse-brain-atlases-0.5.3.tar.xz)
#		- Requires ../top_level_data (empty to start, requires > 200Gb)
# run:
# 	podman run \
# 		-it \
# 		--rm \
# 		-v ../input_data/opfvta-bids:/usr/share/opfvta_bidsdata \
# 		-v ../reference_data/mouse-brain-templates-0.5.3:/usr/share/mouse_brain_atlases \
# 		-v ../top_level_data/:/root/.scratch
# 		${FQDN_IMAGE}
#
# # Use this to run a shell
# handtest:
# 	podman run \
# 		-it \
# 		-v input_data:/usr/share/opfvta_bidsdata \
# 		-v reference_data:/TODOWHEREDOESTHISGO \
# 		-v output:/root/.scratch \
# 		${FQDN_IMAGE} \
# 		/bin/bash

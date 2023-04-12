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




######## Containerized ########

# We must allow others exactly use our script without modification
# Or its not replicable by others.
#
REGISTRY=docker.io
REPOSITORY=asmacdo

IMAGE_NAME=opfvta
IMAGE_TAG=2.0.0-alpha

INPUT_NAME=opfvta_bidsdata
INPUT_TAG=2.1.0-alpha

REFERENCE_NAME=mouse_templates_atlases
REFERENCE_TAG=1.0.0-alpha

FQDN_IMAGE=${REGISTRY}/${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}
FQDN_INPUT_DATA=${REGISTRY}/${REPOSITORY}/${INPUT_NAME}:${INPUT_TAG}
FQDN_REFERENCE_DATA=${REGISTRY}/${REPOSITORY}/${REFERENCE_NAME}:${REFERENCE_TAG}
# Build and push to both?
# APPTAINER_REGISTRY=""

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

# build-opfvta-bidsdata:
# 	podman build . \
# 		-f ../input_data/Containerfile \
# 		-t ${FQDN_INPUT_DATA}

# build-mouse-templates-atlases:
# 	podman build . \
# 		-f ../reference_data/Containerfile \
# 		-t ${FQDN_REFERENCE_DATA}



# TODO RM
# push-dev-only:
# 	podman push ${FQDN_IMAGE}
# 	podman push ${FQDN_INPUT_DATA}
# 	podman push ${FQDN_REFERENCE_DATA}

push:
	podman push ${FQDN_IMAGE}

# mouse-volume: build-mouse-templates-atlases
# 	podman volume rm input_data -f
# 	# IDK if this hack actually works
# 	podman volume create input_data
# 	# Its annoying I have to run a container for this? Can i endit?
# 	podman run \
# 		-d \
# 		-it \
# 		--rm \
# 		-v input_data:/input_volume \
# 		${FQDN_INPUT_DATA} \
# 		/bin/sh
#
# scatch:
# 	podman volume create output

# Notice this doesnt drop you into a shell and the container is deleted after use
run:
	podman run \
		-it \
		--rm \
		-v ../input_data/opfvta-bids:/usr/share/opfvta_bidsdata \
		-v ../reference_data/mouse-brain-templates-0.5.3:/usr/share/mouse_brain_atlases \
		-v ../top_level_data/:/root/.scratch
		${FQDN_IMAGE}

# Use this to run a shell
handtest:
	podman run \
		-it \
		-v input_data:/usr/share/opfvta_bidsdata \
		-v reference_data:/TODOWHEREDOESTHISGO \
		-v output:/root/.scratch \
		${FQDN_IMAGE} \
		/bin/bash

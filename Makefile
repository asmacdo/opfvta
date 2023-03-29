base:
	podman build . -f Containerfile.base -t thebase:2023

science:
	podman build . -f Containerfile -t science-time:typhon1

all: base science
	echo "ALL"


RT_PROFILE=~/utils/histology.pp3
echo "Repositing histology files from ${1} to ${2}."

pushd $1
mkdir "${1}/.old/"
for i in *.TIF; do
	mkdir "${2}/${i%%_*_*_*.TIF}"
	echo "Copying ${i} to new location..."
	cp "${i}" "${2}/${i%%_*_*_*.TIF}"
	echo "Moving ${i} to ${1}/.old archive..."
	mv "${i}" "${1}/.old/"
	pushd "${2}/${i%%_*_*_*.TIF}"
	echo "Unpacking ${i} ..."
	convert "${i}" -scene 1 "${i%%.TIF}%d.tif"
	rm "${i}"
	echo "Exporting ${i%%.TIF}.tif ..."
	rawtherapee-cli -n -p $RT_PROFILE -Y -c "${i%%.TIF}"*.tif
	popd
done
popd

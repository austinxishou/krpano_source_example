#!/bin/bash


shopt -s nullglob

#find "../media/Backup 斯里兰卡" -type d | while read dir; do
find "${1}" -type d | while read dir; do
	if [[ "$dir" =~ "vtour" ]]; then
		rm -rf $dir
	fi
	files=("$dir"/*.jpg)
	if [ ${#files[@]} -gt 0 ]; then
		if ! [[ $files =~ \* ]]; then
			echo "${files[@]//*thumb*/}"
			/opt/krpano-1.19-pr12/krpanotools makepano -config=/opt/krpano-1.19-pr12/templates/vtour-normal.config "${files[@]//*thumb*/}"
			rm "${files[@]//*thumb*/}"
		fi
	fi
done




#shopt -s nullglob
#find "$1" -type d | while read dir; do
#	if [ "$dir" -eq "vtour" ]; then
#		rm -rf $dir
#	fi
#	files=("$dir"/*.jp*g)
#	if [ ${#files[@]} -gt 0 ]; then
#		echo "${files[@]}"
#		krpano.bat "${files[@]}"
#	fi
#done



###### how to use #######

# dir
#  |---subdir1
#  |     |-----ssubdir
#  |     |-----file1
#  |---subdir2
#  |---file1
#  |---krpano.sh

# execute ./krpano.sh to generate vtour folder with panorama

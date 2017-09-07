#!/bin/sh


if [[ "$sys" == "Linux" ]]; then
	qshell=qshell_linux_amd64
else
	qshell=qshell_darwin_amd64
fi

find common -type f | while read file; do
	if [[ $file =~ DS_Store ]]; then
		continue
	fi
	$qshell fput "$1" "${file}" "${file}"
done


####### How to use ########

# dir
#  |----common
#  |----uploadCommon.sh

# execute ./uploadCommon.sh spaceOf7niu to upload the common files which contains all common files used by krpano and utovr
# each spaceOf7niu should have one

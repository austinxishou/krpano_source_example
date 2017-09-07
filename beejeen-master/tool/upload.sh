#!/bin/bash

list=()
for (( i=2; i<=$#; i++ )) ; do
	list+=("${!i}")
done

spaceName="$1"
echo "${list[@]}" "will be uploaded to $spaceName. Are you sure? y/n:"
read answer
if [[ ! "$answer" =~ ^y.* && ! "$answer" =~ ^Y.* ]]; then
	echo "Please edit main.sh and redefine the variable files."
	exit 0
fi

content=$spaceName".list"

temps=`date +%s`
sys=`uname`

if [[ "$sys" == "Linux" ]]; then
	qshell=qshell-linux-x64
	#qshell=qshell_linux_amd64
	sed=sed
else
	qshell=qshell_darwin_amd64
	sed=gsed
fi

echo "geting content from 7niu..."
$qshell listbucket $spaceName $content

$sed -i -e $'s/\t.*//' $content

for param in "${list[@]}"; do
	echo "==================================== upload ${param}... ===================================="
	find "$param" -type f | while read newFile; do
		if [[ "$newFile" =~ DS_Store ]]; then
			continue
		fi
		if [[ $newFile =~ pano_.*jpg ]]; then
			echo 'add watermark for' "$newFile"
			python3.6 encode.py --image "$newFile" --watermark watermark.jpg --result "$newFile"
		fi
		while IFS='' read -r oldFile || [[ -n "$oldFile" ]]; do
			if [[ "${oldFile#*/}" =~ "${newFile}" ]]; then
				echo "delete" "$oldFile" "from" "$spaceName"
				$qshell delete $spaceName "$oldFile"
				break
			fi
		done < $content
		echo "upload" "${temps}/${newFile}" "to ${spaceName}"
		$qshell fput $spaceName "${temps}/${newFile}" "${newFile}"
	done
done


echo "geting current content from 7niu..."
$qshell listbucket $spaceName $content

$sed -i -e $'s/\t.*//' $content


$sed -i -e '/html\|Thumb[^\/]*\.jpg\|.*\.mp3/!d' "$content"
$sed -i -e '/editor/d' "$content"

url="http://"$spaceName".beejeen.com/"
$sed -i -e "s#^#${url}#g" "$content"
$sed -i -e 's# #%20#g' "$content"





####### How to use ########

# dir
#  |----subdir1
#  |----subdir2
#  |----upload.sh

# execute ./upload.sh spaceOf7niu subdir1 subdir2 to upload the directories to a space of 7niu as below:
# <time>/dir/subdir1/...
# <time>/dir/subdir2/...

# if file exists in 7niu, delete it and upload the current one
# else upload the new file

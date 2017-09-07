#!/bin/sh

num=0

while IFS= read -r myfile; do
	if [[ $myfile =~ .project || $myfile =~ .swf || $myfile =~ jpg || $myfile =~ .gif || $myfile =~ .git || $myfile =~ log || $myfile =~ DS_Store || $myfile =~ .png || $myfile =~ .ico ]]; then
		continue
	fi

	a=$(cat "${myfile}" | wc -l)
	num=$(( $num + $a ))
done <<< "$( find . -type f )"
echo $num


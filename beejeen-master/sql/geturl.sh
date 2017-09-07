#!/bin/sh


######## this should be an argument
spaceName="$1"
content=$spaceName".list"

sys=`uname`

if [[ "$sys" == "Linux" ]]; then
	qshell=qshell_linux_amd64
	sed=sed
else
	qshell=qshell_darwin_amd64
	sed=gsed
fi

echo "geting current content from 7niu..."
$qshell listbucket $spaceName $content


$sed -i -e $'s/\t.*//' $content

$sed -i -e '/html\|Thumb[^\/]*\.jpg\|.*\.mp3/!d' "$content"
$sed -i -e '/editor/d' "$content"

url="http://"$spaceName".beejeen.com/"
$sed -i -e "s#^#${url}#g" "$content"
$sed -i -e 's# #%20#g' "$content"

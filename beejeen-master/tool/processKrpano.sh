#!/bin/bash

tool="processXML.out"

g++ -std=c++11 processXML.cpp -o "$tool"

if [[ "$sys" == "Linux" ]]; then
	sed=sed
else
	sed=gsed
fi

find . -type f -print0 | while IFS= read -r -d '' myfile; do
	if [[ $myfile =~ tour\.xml ]]; then
		echo "Processing:" "$myfile"
		num=$(echo "$myfile" | tr -cd '/' | wc -c)
		if [[ $myfile =~ Thumb.* ]]; then
			./$tool "$myfile" $num "Thumb"
		else
			./$tool "$myfile" $num
			sed -i "s# onstart=\"#&js(getComment(get(xml.scene)));#" "$myfile"
			#sed -i '' "s# onstart=\"#&js(getComment(get(xml.scene)));#" "$myfile"
		fi
	fi
	if [[ $myfile =~ Thumb.*tour\.html ]]; then
		echo "Processing:" "$myfile"
		sed -i "s#true.*#true,mwheel:false});#" "$myfile"
		#sed -i '' "s#true.*#true,mwheel:false});#" "$myfile"
	fi
	if [[ $myfile =~ vtour/tour.*\.html ]]; then
		if grep -q "common" "$myfile"; then
			continue
		fi
		num=$(echo "$myfile" | tr -cd '/' | wc -c)
		path=""
		for(( i=0; i<=$num; i++ )); do
			path="$path../"
		done
		path="${path}common"
		path2="${path}/"
		if [[ $myfile =~ Thumb.* ]]; then
			## &: insert
			sed -i "s#src=\"#&${path2}#" "$myfile"
			#sed -i '' "s#src=\"#&${path2}#" "$myfile"
			sed -i "s#swf:\"#&${path2}#" "$myfile"
			#sed -i '' "s#swf:\"#&${path2}#" "$myfile"
			sed -i "s#plugins#${path2}&#" "$myfile"
			#sed -i '' "s#plugins#${path2}&#" "$myfile"
			continue
		fi
		echo "Processing:" "$myfile"
		cp "${myfile##*/}" "${myfile%/*}/"
		sed -i "s#ZZZZZZZ#${path}#" "$myfile"
		#sed -i '' "s#ZZZZZZZ#${path}#" "$myfile"
	fi
done

rm $tool


####### How to use ########

# dir
#  |----country
#  |----processKrpano.sh
#  |----processKrpano.cpp

# execute ./processKrpano.sh to edit all tour.xml and tour.html to:
# tour.xml:
#	remove krpano-title name by default
#	make krpano-scene rotate automatically
#	remove Google Earth icon
#	make thumbs open automatically if it's not a Thumb
#   set transparency of tool bar
#	make krpano-scenes in order
# tour.html:
#	disable wheel if it's a Thumb
# vtour/skin/vtourskin.png:
#	replace this png with ./vtourskin.png

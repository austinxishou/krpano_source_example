#!/bin/bash


find video_utovr/video -type f -print0 | while IFS= read -r -d '' myfile; do
	# remove ./ at the beginning
	#myfile=${myfile:2}
	if [[ $myfile =~ .*\.DS_Store ]]; then
		continue
	fi
	echo "Processing:" "${myfile%.*}.html"
    tmp=$(basename "$myfile")   #example.mp4
    tmpmp4=$(basename "$myfile")   #example.mp4
	#tmp="${tmp/.mp4/.html}"     #example.html
	name="${tmp/.mp4/}"     #example
	#myfile="${myfile#*/}"    #remove video_utovr/ from the path
	tmp="${myfile%.*}.html"
	cp -rf video_utovr/index.html "${tmp}"



	sed -i "s#sceneName:.*#sceneName: \"${name//&/\\&}\",#" "$tmp"
	#sed -i '' "s#sceneName:.*#sceneName: \"${name//&/\\&}\",#" "$tmp"
	sed -i "s#sceneFilePath:.*#sceneFilePath: \"./${tmpmp4}\",#" "$tmp"
	#sed -i '' "s#sceneFilePath:.*#sceneFilePath: \"./${tmpmp4}\",#" "$tmp"

	#pathPlayer="./../common"
	num=$(echo "$tmp" | tr -cd '/' | wc -c)
	pathPlayer="./"
	for(( i=0; i<$num; i++ )); do
		pathPlayer="$pathPlayer../"
	done
	pathPlayer="${pathPlayer}common"


	sed -i "s#src=\".#&${pathPlayer}#" "$tmp"
	#sed -i '' "s#src=\".#&${pathPlayer}#" "$tmp"
done




####### How to use ########

# dir
#  |----player <--- coming from utovr
#  |----video <--- put all videos and/or subdirs in it
#  |----generateIndex.sh
#  |----index.html <--- coming from utovr, name must be index.html

# execute ./dir/generateIndex.sh to generate all html files for each video

# ATTENTION: this script must be executed from its upper directory meaning from the dir.

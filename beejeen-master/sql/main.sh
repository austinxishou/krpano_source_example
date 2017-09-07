#!/bin/sh


./backup.sh

if [[ "$1" == "csv" ]]; then
	mysql -f -h "localhost" -u "root" "-ppassword" "dbbj" < "import_csv.sql"
	if [[ $# == 2 ]]; then
		file=${2}
		mysql -h "localhost" -u "root" "-ppassword" "dbbj" < "$file"
	fi
elif [[ "$1" == "url" ]]; then
	./geturl.sh "$2"
	#mysql -h "localhost" -u "root" "-ppassword" "dbbj" < "update_url.sql"
	#mysql -h "localhost" -u "root" "-ppassword" "dbbj" -e "set @spaceName=\"$1\";source update_url2.sql;"
	file=${2}.list
	if [[ "$2" == "travel" || "$2" == "chosen" ]]; then
		sed s/%fileName%/${file}/ update_$2.sql | mysql -h "localhost" -u "root" "-ppassword" "dbbj"
	else
		sed s/%fileName%/${file}/ update_url.sql | mysql -h "localhost" -u "root" "-ppassword" "dbbj"
	fi
elif [[ "$1" == "poi" ]]; then
	mysql -f -h "localhost" -u "root" "-ppassword" "dbbj" < "generatePOI.sql"
fi



############ how to use ##############

# execute ./main.sh csv country to import csv and update ad_cost
# execute ./main.sh url continent to get url file from 7niu and import the file into database

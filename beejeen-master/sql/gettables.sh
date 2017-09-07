#!/bin/sh


tables=( "Country" "City" "Activity" "Restaurant" "Hotel" "Sight" )
tablesColumns=()
for element in "${tables[@]}"; do
	tablesColumns+=(${element}Column.csv)
done
for ((i = 0; i < ${#tables[@]}; ++i)); do
	rm -f /var/lib/mysql-files/${tablesColumns[$i]}
	mysql -f -h "localhost" -u "root" "-ppassword" "dbbj" -e "show columns from ${tables[$i]} into outfile \"/var/lib/mysql-files/${tablesColumns[$i]}\" FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n';"
done


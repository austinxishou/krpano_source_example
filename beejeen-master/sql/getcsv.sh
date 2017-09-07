#!/bin/sh

rm -f /var/lib/mysql-files/$1.csv
mysql -f -h "localhost" -u "root" "-ppassword" "dbbj" -e "select * from $1 into outfile \"/var/lib/mysql-files/$1.csv\" FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n';"
echo /var/lib/mysql-files/$1.csv generated.

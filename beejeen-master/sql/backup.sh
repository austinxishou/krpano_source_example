#!/bin/sh


echo "backup for database..."
mysqldump -u root -ppassword dbbj > dbbj.sql

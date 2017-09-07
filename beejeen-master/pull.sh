#!/bin/sh

echo 'update master...'
if [[ $# == 1 ]]; then
	git add --all
	git commit -m "$1"
fi

echo 'check to branch frontend'
git checkout frontend

echo 'pull...'
git pull

echo 'check to branch master'
git checkout master

echo 'merge frontend to master...'
git merge --no-ff frontend

echo 'server restarting...'
pkill -f mainbj.py
nohup /var/server/beejeen/mainbj.py >/dev/null 2>nohup.log &
pkill -f sslmainbj.py
nohup /var/server/beejeen/sslmainbj.py >/dev/null 2>nohup.log &

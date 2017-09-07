#!/bin/sh


if [[ $1 == '' ]]; then
	fois=200
else
	fois=$1
fi
y=0
x=0
i=0
while [ $i -lt $fois ]; do
	tput cup $y $x
	echo ''
	echo ''
	echo ''
	echo '============== current time ==============='
	echo $i
	echo '==========================================='
	echo ''
	curl -i http://www.beejeen.com/html/country-cn.html/index?key=abceefgefwe
	curl -i http://www.beejeen.com/html/country-cn.html?croatiacontent
	i=$((i+1))
done

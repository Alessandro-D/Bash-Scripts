#!/bin/bash

# Arguments
IP=$1

# Setup
mkdir -p /tmp/ip-search/
touch /tmp/ip-search/description.html

# Execution
if
	[ $IP != "0.0.0.0" ]; 
then
	wget -q -O /tmp/ip-search/description.html db-ip.com/$IP && 
		cat /tmp/ip-search/description.html | 
		grep -i description | 
		head -n 1 | 
		cut -d'"' -f 4 |
		cut -d'(' -f 1
else
	echo "Not a valid IP"
fi

# Cleanup
rm /tmp/ip-search/description.html
rmdir /tmp/ip-search

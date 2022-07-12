#!/bin/bash

PATH_TO_STORE="archives/"
PATH_TO_DATA="test/"
#PATH_TO_STORE="/homes/aab621/eWater-uploads/"
#PATH_TO_DATA="/vol/bitbucket/aab621/eWater-uploads/"

if [ ! -d ${PATH_TO_STORE} ]; then
	mkdir ${PATH_TO_STORE}
fi

# Tar files
timestamp="$(date '+%F_%T')"
tar -cvpzf ${PATH_TO_STORE}${timestamp}.tar.gz ${PATH_TO_DATA}

# Delete files after compression
rm ${PATH_TO_DATA}*

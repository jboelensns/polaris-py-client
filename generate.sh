#!/bin/bash
set -e

#
#
#wget --no-check-certificate http://localhost:8989/apispec_1.json
#
#
#

if [ -z "$1" ]
then
	FILENAME="apispec_1.json"
else
    URL="https://api.polaris.nskope.net/apispec_1.json"
	FILENAME="$(basename -- $URL)"
	rm $FILENAME
	wget --no-check-certificate $URL
fi

echo "Generating file from $URL ($FILENAME)"

VERSION=$(/usr/bin/jq '.info.version' $FILENAME.json | perl -pe 's/(\d*.\d*.\d*)-(\d*)-(.*)/$1+$2.$3/' )
PKG_NAME="polarisgenclient"
PROJ_NAME="polaris-gen-client"

echo "{\"packageVersion\": $VERSION, \"projectName\": \"$PROJ_NAME\",\"packageName\":\"$PKG_NAME\"}" > config.json

cat config.json
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/$FILENAME -l python -o /local/ -c /local/config.json

# copy our helpers into the package
cp include/* $PKG_NAME/
sudo sed -i 's/PKG_NAME/polarisgenclient/g' $PKG_NAME/*.py

# the requirements are written by the generator every time
# we want to keep our requirements
cp requirements.all requirements.txt

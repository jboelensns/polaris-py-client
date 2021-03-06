#!/bin/bash
set -e

# TODO: operationId's need to be added to each endpoint
#
# generate.sh
# 
# uses a docker container to generate a python client for the polaris api
#
# usage: sudo ./generate.sh [url_to_spec_file]
#
# e.g 
#  - use the prod spec
#  generate.sh https://api.polaris.nskope.net/apispec_1.json
#  - use a local dev spec
#  generate.sh http://localhost:8989/apispec_1.json
#  - use the spec file committed to the repo (apispec_1.json) 
#  generate.sh 
#

if [ -z "$1" ]
then
	FILENAME="apispec_1.json"
else
    URL=$1
    # example URL="https://api.polaris.nskope.net/apispec_1.json"
	FILENAME="$(basename -- $URL)"
    mv $FILENAME "$FILENAME.old" || true
	wget --no-check-certificate $URL
fi

echo "Generating file from $URL ($FILENAME)"

VERSION=$(/usr/bin/jq '.info.version' $FILENAME | perl -pe 's/(\d*.\d*.\d*)-(\d*)-(.*)/$1+$2.$3/' )
PKG_NAME="polarisgenclient"
PROJ_NAME="polaris-gen-client"

echo "{\"packageVersion\": $VERSION, \"projectName\": \"$PROJ_NAME\",\"packageName\":\"$PKG_NAME\"}" > config.json

cat config.json
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/$FILENAME -l python -o /local/ -c /local/config.json

# copy our helpers into the package
cp include/* $PKG_NAME/
sudo sed -i 's/PKG_NAME/polarisgenclient/g' $PKG_NAME/*.py

# cleanup generated stuff we don't care about
set +e
rm -r .swagger-codegen/
rm .travis.yml
rm config.json
rm git_push.sh
rm test-requirements.txt
rm -r test/
rm tox.ini

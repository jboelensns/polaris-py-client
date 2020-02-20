#!/bin/bash

set -e

#
# validate.sh
# 
# uses a docker container to validate the polaris api spec file
#
# usage: sudo ./validate.sh [url_to_spec_file]
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
	rm $FILENAME
	wget --no-check-certificate $URL
fi

echo "Validating file from $URL ($FILENAME)"

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli validate -i /local/$FILENAME


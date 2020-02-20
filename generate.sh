#!/bin/bash

set -e

# rm -rf swagger.json
# wget --no-check-certificate https://polaris-provisioner.polaris.192.168.2.196.xip.io/swagger.json

#rm -rf apispec_1.json
#wget --no-check-certificate http://localhost:8989/apispec_1.json

VERSION=$(/usr/bin/jq '.info.version' apispec_1.json | perl -pe 's/(\d*.\d*.\d*)-(\d*)-(.*)/$1+$2.$3/' )

echo "{\"packageVersion\": $VERSION, \"projectName\": \"polaris-api\",\"packageName\":\"polarisapi\"}" > config.json

cat config.json
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/apispec_1.json -l python -o /local/ -c /local/config.json

#!/bin/bash

set -e

#rm -rf apispec_1.json
#wget --no-check-certificate http://localhost:8989/apispec_1.json

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli validate -i /local/apispec_1.json


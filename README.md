# Overview

This project containers the tools required to generate a python client for the Polaris API as well as the client itself.

Code generation is executed by way of swagger-codegen inside of a docker container.

## Scripts

There are three important scripts included:

.: **[generate.sh](generate.sh)**

Uses the docker container to generate the client based on the spec file.

Optionally a url may be provided.  If provided, the file will be fetched and generation will occur based on it.

```
# run against the locally committed apispec_1.json file
sudo ./generate.sh http://localhost:8989/apispec_1.json
```

```
# run against a local dev api
sudo ./generate.sh http://localhost:8989/apispec_1.json
```

```
# run against the prod api
sudo ./generate.sh https://api.polaris.nskope.net/apispec_1.json
```

.: **[validate.sh](validate.sh)**

Uses the docker container to validate the spec file for correctness

Optionally a url may be provided.  If provided, the file will be fetched and validation will occur based on it.

```
# run against the locally committed apispec_1.json file
sudo ./validate.sh http://localhost:8989/apispec_1.json
```

```
# run against a local dev api
sudo ./validate.sh http://localhost:8989/apispec_1.json
```

```
# run against the prod api
sudo ./validate.sh https://api.polaris.nskope.net/apispec_1.json
```

.: **[clean.sh](clean.sh)**

Removes all of the generated code

```
.: **[clean.sh](clean.sh)**
```

## Samples

Two helper files have been included in order to make constructing clients able to authenticate with `jwt` easier.

.: **[sample_client.py](sample_client.py)**

This client illustrates the usage of the helpers to create an ArpClient and get a list of arp records.

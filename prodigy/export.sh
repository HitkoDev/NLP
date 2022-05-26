#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp registry.htk.io/ds/prodigy "prodigy db-out stories /nlp/out"

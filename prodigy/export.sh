#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy db-out stories /nlp/out"

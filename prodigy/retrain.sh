#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.batch_train stories /nlp/en_core_web_lg_base -o /nlp/en_core_web_lg_rt -n 10"

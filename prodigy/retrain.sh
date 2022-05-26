#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp registry.htk.io/ds/prodigy "prodigy ner.batch_train stories /nlp/en_core_web_lg_base -o /nlp/en_core_web_lg_rt -n 10"

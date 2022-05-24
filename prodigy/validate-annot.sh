#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/all.jsonl --label PERSON -U"

#!/bin/bash
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy dataset stories"
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy db-in stories /nlp/tokenized/all.jsonl"
docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.batch_train stories en_core_web_lg -o /nlp/en_core_web_lg_base -n 10"
mv dataset/prodigy.db dataset/prodigy.base.db
cp -rT dataset/en_core_web_lg_base dataset/en_core_web_lg_rt

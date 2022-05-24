#!/bin/bash

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/a-gift-for-terra.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/ashputtel.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/coming-attraction.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/freddie.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/hills-like-white-elephants.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/home.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/leiningen-vs-the-ants.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/soraya.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/tania-in-a-winter-wonderland.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/the-canterville-ghost.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/the-gift-of-the-magi.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/the-iron-lady.jsonl --label PERSON -U"

docker run -ti --rm -v $(pwd)/dataset:/nlp -p 3000:3000 registry.htk.io/ds/prodigy "prodigy ner.make-gold stories /nlp/en_core_web_lg_rt /nlp/tokenized/the-ransom-of-red-chief.jsonl --label PERSON -U"

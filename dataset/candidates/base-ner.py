# # Extract persons
#
# Go through candidate stories and find those with at least 4 named persons. Persons are extracted using Spacy's Bert-based model.

# +
import spacy

nlp = spacy.load("en_core_web_trf")

# +
import glob
import json
import pathlib

from tqdm.notebook import tqdm

pathlib.Path("../tokenized").mkdir(parents=True, exist_ok=True)

files = glob.glob('./*.txt')

all_rows = []
all_sent = []

sp = {" ", "."}

for file in files:
    target = file.replace('./', '../tokenized/').replace('.txt', '.jsonl')

    with open(file, 'r') as f:
        sentences = f.read().split('\n')

    s = []
    for sss in sentences:
        if len(s) > 0 and s[-1].endswith('.') and s[-1][-2] not in sp:
            s[-1] = '{} {}'.format(s[-1], sss)
        else:
            s.append(sss)

    sentences = s

    print(file)
    persons = set()
    rows = []
    sents = []
    for i in tqdm(sentences):
        if len(i):
            doc = nlp(i)
            out = {
                "text": str(doc),
                "meta": dict(source=file),
                "tokens": [{"text": str(t), "start": t.idx, "end": t.idx + len(str(t)), "id": t.i} for t in doc],
                "spans": [{"label": p.label_, "start": p.start_char, "end": p.end_char, "token_start": p.start, "token_end": p.end - 1} for p in doc.ents if p.label_ == 'PERSON']
            }
            out = json.dumps(out)
            rows.append(out)
            sents.append(i)

        for p in doc.ents:
            if p.label_ == 'PERSON':
                persons.add(p.text)

    if len(persons) > 3:
        with open(target, 'w') as f:
            f.write('\n'.join(rows))

        target = file.replace('./', '../tokenized/')
        with open(target, 'w') as f:
            f.write('\n'.join(sentences))

        target = target.replace('.txt', '.persons.txt')
        with open(target, 'w') as f:
            f.write('\n'.join(persons))

        all_rows.append('\n'.join(rows))
        all_sent.append('\n'.join(sents))
    else:
        print('skip')

with open('../tokenized/all.jsonl', 'w') as f:
    f.write('\n'.join(all_rows))

with open('../tokenized/all.txt', 'w') as f:
    f.write('\n'.join(all_sent))
# -



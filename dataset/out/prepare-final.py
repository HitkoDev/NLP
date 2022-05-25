# +
import json

with open('./stories.jsonl', 'r') as file:
    lines = file.read().split('\n')

mps = {}
for l in lines:
    try:
        d = json.loads(l)
        f = d['meta']['source'].replace('.txt', '.json')
        if f not in mps:
            mps[f] = []

        mps[f].append(d)
    except:
        pass

for f, v in mps.items():
    sents = []
    vertexSet = []
    for i, l in enumerate(v):
        sents.append({"id": i, "v":[t['text'] for t in l['tokens']]})
        for t in l['spans']:
            tx = l['tokens'][t["token_start"]:t["token_end"] + 1]
            text = ' '.join([x['text'] for x in tx])
            vertexSet.append({
                "name": t.get('text', text),
                "sent_id": i,
                "type": "PER",
                "pos": [
                    t["token_start"],
                    t["token_end"] + 1
                ]
            })

    vm = {}
    for v in vertexSet:
        n = v['name']
        if n not in vm:
            vm[n] = []

        vm[n].append(v)

    with open(f, 'w') as file:
        file.write(json.dumps({
            "title": f,
            "sents": sents,
            "vertexSet": list(vm.values())
        }))

    with open(f.replace('.json', '.persons.json'), 'w') as file:
        file.write(json.dumps({
            "persons": [[k] for k in vm],
            "relations": [{"from": "", "to": "", "label": "", "evidence": []}]
        }))
# -

# ### At this point `.persons.json` files have been generated; edit those files to group all names which belong to the same person

# +
import glob
import json
import pathlib

pathlib.Path("../final/stories").mkdir(parents=True, exist_ok=True)

files = glob.glob('./*.persons.json')

for f in files:
    with open(f, 'r') as file:
        persons = json.loads(file.read())

    fr = f.replace('.persons.json', '.json')
    with open(fr, 'r') as file:
        data = json.loads(file.read())

    pd = {}
    pds = []
    for i, ps in enumerate(persons['persons']):
        pds.append([])
        for p in ps:
            pd[p] = i

    labels = []
    for r in persons['relations']:
        if len(r['from']):
            labels.append({
                "r": r['label'],
                "h": pd[r['from']],
                "t": pd[r['to']],
                "evidence": r['evidence']
            })

    data['labels'] = labels
    data['sents'] = [k['v'] for k in data['sents']]
    for d in data['vertexSet']:
        for l in d:
            if l['name'] in pd:
                pds[pd[l['name']]].append(l)

    data['vertexSet'] = pds

    with open(fr.replace('./', '../final/stories/'), 'w') as file:
        file.write(json.dumps(data))
# -



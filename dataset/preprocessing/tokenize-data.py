import sys
# !conda install --yes --prefix {sys.prefix} spacy nltk tqdm spacy-transformers

# +
import nltk

nltk.download('punkt')
# #!spacy download en_core_web_sm

# +
import spacy

nlp = spacy.load("en_core_web_trf")

# +
import glob
import re

from nltk.tokenize import sent_tokenize
from tqdm.notebook import tqdm

files = glob.glob('../stories/*.md')

for file in files:
    with open(file, 'r') as f:
        text = f.read().replace('. . .', '...').replace('`', "'").replace('´', "'").replace(
            '‘', "'").replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('…', '...').replace('""', "''")

    print(file)
    sentences = []
    persons = set()
    for i in tqdm(sent_tokenize(text)):
        doc = nlp(re.sub('\\s+', ' ', i).strip())
        sentences.append(' '.join([str(t) for t in doc]))
        for p in doc.ents:
            if p.label_ == 'PERSON':
                persons.add(p.text)

    target = file.replace('stories', 'tokenized').replace('.md', '.txt')
    with open(target, 'w') as f:
        f.write('\n'.join(sentences))

    target = target.replace('.txt', '.persons.txt')
    with open(target, 'w') as f:
        f.write('\n'.join(persons))
# -


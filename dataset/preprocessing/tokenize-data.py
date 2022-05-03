import sys
# !conda install --yes --prefix {sys.prefix} spacy nltk tqdm

# +
import nltk

nltk.download('punkt')

# +
import glob
import re

import spacy
from nltk.tokenize import sent_tokenize
from tqdm.notebook import tqdm

nlp = spacy.load("en_core_web_sm")

files = glob.glob('../stories/*.md')

for file in tqdm(files):
    with open(file, 'r') as f:
        text = f.read().replace('. . .', '...').replace('`', "'").replace('´', "'").replace(
            '‘', "'").replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('…', '...')

    sentences = '\n'.join([' '.join([str(t) for t in nlp(re.sub('\\s+', ' ', i).strip())]) for i in sent_tokenize(text)])
    with open(file.replace('stories', 'tokenized').replace('.md', '.txt'), 'w') as f:
        f.write(sentences)
# -



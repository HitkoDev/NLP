# # Load Grimm stories from dataset
#
# <https://www.kaggle.com/datasets/tschomacker/grimms-fairy-tales>

# +
import re

import pandas as pd

stories = pd.read_csv('./grimm/grimms_fairytales.csv')
for i, r in stories.iterrows():
    n = r['Title'].lower()
    n = re.sub('[^\\w\\d]+', '-', n)
    f = './grimm/{}.md'.format(n)
    with open(f, 'w') as file:
        file.write(r['Text'])
# -

# # Load short stories from project Gutenberg
#
# <https://www.kaggle.com/shubchat/1002-short-stories-from-project-guttenberg>

# +
import re

import pandas as pd

stories = pd.read_csv('./short-stories/db_books.csv')
stories_cont = pd.read_csv('./short-stories/stories.csv', delimiter=',')

for i, r in stories.iterrows():
    n = r['Title'].lower()
    n = re.sub('[^\\w\\d]+', '-', n)
    n = re.sub('^-|-$', '', n)
    f = './short-stories/{}.md'.format(n)
    s = stories_cont[stories_cont['bookno'] == r['bookno']]
    with open(f, 'w') as file:
        file.write(list(s['content'])[0])
# -

# # Normalise & tokenize the stories

# +
import nltk

nltk.download('punkt')

# +
import spacy

nlp = spacy.load("en_core_web_sm")

# +
import glob
import os
import pathlib
import re

from nltk.tokenize import sent_tokenize
from tqdm.notebook import tqdm

pathlib.Path("../normalised").mkdir(parents=True, exist_ok=True)

files = glob.glob('./*/*.md')

for file in files:
    with open(file, 'r') as f:
        text = f.read().replace('. . .', '...').replace('`', "'").replace('´', "'").replace(
            '‘', "'").replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('…', '...').replace("''", '"').replace('_', ' ').replace('\\', ' ')
        text = re.sub('-+', ' - ', text)
        text = re.sub('\*+', ' ', text)

    print(file)
    sentences = []

    sent = sent_tokenize(text)

    if len(sent) > 1000:
        # Exclude all collections etc.
        continue

    for i in tqdm(sent):
        doc = nlp(re.sub('\\s+', ' ', i).strip())
        sentences.append(' '.join([str(t) for t in doc]))

    basename = os.path.basename(file).replace('.md', '.txt')

    target = '../normalised/{}'.format(basename)
    with open(target, 'w') as f:
        f.write('\n'.join(sentences))
# -

# # Filter stories
#
# Count family relations of interest, sort stories by the number of those relations. If at least 10% sentences contain target words, label stories as candidates.

# +
import glob
import pathlib
import shutil

from tqdm.notebook import tqdm

pathlib.Path("../candidates").mkdir(parents=True, exist_ok=True)

files = glob.glob('../normalised/*.txt')

# wirds indicating target relations
rel_words = set([
    "husband",
    "wife",
    "son",
    "daughter",
    "brother",
    "sister",
    "grandpa",
    "grandma",
    "grandson",
    "granddaughter",
    "mother",
    "father",
    "uncle",
    "aunt",
    "nephew",
    "niece",
    "cousin"
])

items = {}
for file in tqdm(files):
    with open(file, 'r') as f:
        text = f.read().split('\n')

    words = [w.lower() for s in text for w in s.split(' ')]
    count = sum([1 for w in words if w in rel_words])
    items[file] = count / len(text)

for k, v in items.items():
    # Keep stories with target relations in at least 10% of the sentences
    if v > 0.1:
        shutil.copy(k, k.replace('normalised', 'candidates'))
# -
# ### Some manual work is needed at this point to go throug the candidates and remove intro and any other text that came with the stories, and remove potentially bad candidates / collections of stories
#




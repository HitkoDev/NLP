# Literacy situation models knowledge base creation

Building a knowledge base based on situation models from selected English/Slovene short stories. Knowledge base can focus on a subset of the following inference types: Referential, Case structure role  assignment, Causal antecedent, Superordinate goal, Thematic, Character emotional reaction, Causal consequence, Instantiation of noun category, Instrument, Subordinate goal, State, Emotion of reader, Author's intent.

### Description:

Extraction of concepts/entities/relationships/topics/time-aware data from novels. Creation of a book knowledge base and methods for inference and visualization (e.g. main characters, good/bad characters, "dramski trikotnik" (story grammar), time and space analysis, ...)

### Task:

1.  selection and retrieval of additional books (EN/SL) - 7 English provided,
2.  review and detailed proposal of analysis to be done, 
3.  analysis with evaluations, explanations from narrative texts/stories, for example: causal chain summaries.

## [Provided English books](https://drive.google.com/drive/folders/1M15GSnqONLrVT0TeLkZ12bVlmHHofPII):

-   [Henry Red Chief](./dataset/source/original/the-ransom-of-red-chief.md)
-   [Hills Like White Elephants](./dataset/source/original/hills-like-white-elephants.md)
-   [Leiningen Versus the Ants](./dataset/source/original/leiningen-vs-the-ants.md)
-   [The Lady or the Tiger](./dataset/source/original/the-lady-or-the-tiger.md)
-   [The Most Dangerous Game](./dataset/source/original/the-most-dangerous-game.md)
-   [The Tell-Tale Heart](./dataset/source/original/the-tell-tale-heart.md)
-   [The Gift of the Magi](./dataset/source/original/the-gift-of-the-magi.md)

## Additional books:

-   [Project Guttenberg](https://www.kaggle.com/shubchat/1002-short-stories-from-project-guttenberg)
-   [Grimm tales](https://www.kaggle.com/datasets/tschomacker/grimms-fairy-tales)
-   [Family Resemblances](./dataset/source/family/family-resemblances.md)
-   [Freddie](./dataset/source/family/freddie.md)
-   [Home](./dataset/source/family/home.md)
-   [Soraya](./dataset/source/family/soraya.md)
-   [Tania In A Winter Wonderland](./dataset/source/family/tania-in-a-winter-wonderland.md)
-   [The Canterville Ghost](./dataset/source/family/the-canterville-ghost.md)
-   [The Iron Lady](./dataset/source/family/the-iron-lady.md)

# Running the project

Run `docker compose up` to start Jupyter server at <http://localhost:8888>. 

## Dataset preparationm

1.  Load the data: <http://localhost:8888/notebooks/work/dataset/source/extract-data.py>

    Download, extract, and copy Kaggle datasets to `dataset/source/grimm` and `dataset/source/short-stories`, then run the code in the notebook to extract candidate stories.

2.  Cleanup candidate stories

    Some stories have preoject Gutenberg intro data or other text at the begining / end; this needs to be manually removed from stories in `dataset/candidates`. There's a few books with more than one story included in project GUtenberg data; those should be deleted from the candidates folder.

3.  Run base NER: <http://localhost:8888/notebooks/work/dataset/candidates/base-ner.py>

    That generates tokenized stories and inital NER labels generated by Spacy's model, and filters out stories with only a small number of named persons.

4.  Perpare anotations for approval: run `./prodigy/base.sh`

5.  Validate annotations: run `./prodigy/validate-annot.sh`, then go to <http://localhost:3000> and approve / fix NER annotations

6.  Train the final model: run `./prodigy/retrain.sh`

Note: to speed up annotation process, one might stop during step 5, run `./prodigy/retrain.sh`, then restart the step 5.

Note 2: Prodigy is proprieatry addon for Spacy toolkit, but one can use <https://hub.docker.com/r/lixiepeng/prodigy> with some tweaks.

## Dataset for family relations

1.  Export validated annotations from Prodigy: run `./prodigy/export.sh`

2.  Prepare the data: run first script in <http://localhost:8888/notebooks/work/dataset/out/prepare-final.py>

    That exports sentences and persons to `dataset/out`; edit `*.persons.json` file to group names and label relations according to DocRED format (see example)

3.  Prepare final dataset in DocRED format: run the remaining scripts in in <http://localhost:8888/notebooks/work/dataset/out/prepare-final.py>

## DocuNET model

1.  Dataset: copy files from `dataset/final` to `docunet/dataset/stories`

2.  Training: from `docunet` foder, run `./scripts/run_stories.sh`

# References:

-   Casseli, Vossen (2017): The Event StoryLine Corpus: A New Benchmark for Causal and Temporal Relation Extraction ([github](https://github.com/tommasoc80/EventStoryLine), [pdf](https://aclanthology.org/W17-2711.pdf))
-   Nahatame (2020): Revisiting Second Language Readers' Memory for Narrative Texts: The Role of Causal and Semantic Text Relations ([pdf](https://www.tandfonline.com/doi/pdf/10.1080/02702711.2020.1768986))
-   van den Broek (1985): Causal Thinking and the Representation of Narrative Events ([pdf](https://www.researchgate.net/profile/Paul-Van-Den-Broek/publication/222232677_Causal_Thinking_and_the_Representation_of_Narrative_Events/links/59f6f2b2a6fdcc075ec61c75/Causal-Thinking-and-the-Representation-of-Narrative-Events.pdf))
-   Mostafazadeh, Chambers, He, Parikh, Batra, Vanderwende, Kohli, Allen (2016): ​​A Corpus and Cloze Evaluation for Deeper Understanding of Commonsense Stories ([pdf](https://aclanthology.org/N16-1098.pdf))
-   Dasgupta, Saha, Dey, Naskar (2018): Automatic Extraction of Causal Relations from Text using Linguistically Informed Deep Neural Networks ([pdf](https://aclanthology.org/W18-5035.pdf))
-   McNamara (2011): Coh-Metrix: An Automated Tool for Theoretical and Applied Natural Language Processing ([pdf](https://www.researchgate.net/profile/Danielle-Mcnamara/publication/285651904_Coh-Metrix_An_Automated_Tool_for_Theoretical_and_Applied_Natural_Language_Processing/links/5dc45b4b4585151435f2ee91/Coh-Metrix-An-Automated-Tool-for-Theoretical-and-Applied-Natural-Language-Processing.pdf))
-   Zwaan, Magliano, Graesser (1995): Dimensions of Situation Model Construction in Narrative Comprehension ([pdf](https://sites.ualberta.ca/~dmiall/LiteraryReading/Readings/Zwann%20Magliano%20Graesser.pdf))
-   Zwaan (1999): Situation Models: The Mental Leap Into Imagined Worlds ([pdf](https://journals.sagepub.com/doi/pdf/10.1111/1467-8721.00004))

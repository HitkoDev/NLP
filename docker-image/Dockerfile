FROM jupyter/datascience-notebook
RUN pip install \
    jupytext spacy nltk tqdm spacy-transformers && \
    spacy download en_core_web_sm && \
    spacy download en_core_web_trf && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"; 

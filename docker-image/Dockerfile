FROM jupyter/datascience-notebook
RUN mamba install --quiet --yes \
    'jupytext' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"; 
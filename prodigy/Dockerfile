FROM lixiepeng/prodigy
RUN spacy download en_pytt_robertabase_lg
RUN spacy download en_core_web_lg
RUN pip install spacy-pytorch-transformers

VOLUME [ "/nlp" ]
ENV PRODIGY_HOME=/nlp

ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "prodigy ner.make-gold stories en_core_web_lg /nlp/dataset/home.txt --label PERSON" ]

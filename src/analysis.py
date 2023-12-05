import time
import spacy
import requests
from spacy.lang.es.stop_words import STOP_WORDS

nlp = spacy.load("es_core_news_md")

def spacy_analysis(text):
    res = nlp(text)
    tiempo_init = time.time()
    
    etiquetas_pos = [(token.text, token.pos_) for token in res]
    entidades_nombradas = [(ent.text, ent.label_) for ent in res.ents]
    tiempo_fin = time.time() - tiempo_init
    
    a_result = {"etiquetas_pos": etiquetas_pos, 
                "entidades_nombradas": entidades_nombradas,
                 "tiempo_ejecucion": tiempo_fin }
    return a_result


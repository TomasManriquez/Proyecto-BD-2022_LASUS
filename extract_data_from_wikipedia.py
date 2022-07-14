import spacy
import fr_core_news_md

nlp = fr_core_news_md.load()

import wikipedia
wikipedia.set_lang("es")



import pageviewapi
from collections.abc import Mapping
print("wikipedia OK")

from collections import Mapping
import torch

from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)
q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)
print("transformers OK")

import warnings
warnings.filterwarnings("ignore")


text = "Gabriel Boric"

doc = nlp(text)

print("--------------------")

for ent in doc.ents:
    if ((ent.label_ == "PER") and (" " in ent.text)):
        
        #persona mencionada
        person = ent.text
        print(person)

        #resumen wikipedia
        results= wikipedia.search(person)
        summary= wikipedia.summary(results[0], sentences=3)

        #preguntas
        result = q_a_es(question="¿En qué año nació el o ella?", context=summary)
        print("Nació en "+result["answer"])

        result = q_a_es(question="¿Cuál es su profesión?", context=summary)
        print("Su profesión es "+result["answer"])

        result=pageviewapi.per_article('es.wikipedia', person, '20220705', '20220705',
                        access='all-access', agent='all-agents', granularity='daily')

        for item in result.items():
            for article in item[1]:
                views=article['views']
                print("Su popularidad hoy es: "+str(views)+" visitas en wikipedia español.")

        print("--------------------")
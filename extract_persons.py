from typing import TextIO
import spacy
import fr_core_news_md
from scrappers.magallanes_magallanews import text as texto
#import scrappers.magallanes_elmagallanico as A

nlp = spacy.load("es_core_news_md")

import warnings
warnings.filterwarnings("ignore")


#doc = nlp(texto)

print("--------------------")

for i, textual in enumerate(texto):
    doc= nlp(textual)
    persona=[]
    for ent in doc.ents:
        if ((ent.label_ == "PER") and ((" " in ent.text))):
            
            #persona mencionada
            person = ent.text
            #print(person)
            persona.append(person)

            #print("--------------------")

    print(persona)
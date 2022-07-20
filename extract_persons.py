import spacy
from scrappers.magallanes_magallanews import noticias as textos

nlp = spacy.load("es_core_news_md")



print("--------------------")
n=1
for noticia in textos:
    doc = nlp(noticia)
    print("Personas Noticia ",n,":")
    for ent in doc.ents:
        if ((ent.label_ == "PER")):
            
            #persona mencionada
            person = ent.text
            print(person)

    n+=1
    print("--------------------")
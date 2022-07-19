from typing import TextIO
import spacy
import fr_core_news_md
from scrappers.magallanes_elmagallanico import text as texto
#import scrappers.magallanes_elmagallanico as A

nlp = fr_core_news_md.load()

from collections.abc import Mapping, MutableMapping


import warnings
warnings.filterwarnings("ignore")

text = """
El ministro de la Segpres, Giorgio Jackson, se refirió al proyecto que disminuye el quórum para reformar la actual Constitución a 4/7.
La iniciativa, presentada por los senadores Matías Walker y Ximena Rincón (DC), fue aprobada este martes en la comisión de Constitución de la Cámara Alta.
"""

doc = nlp(texto)

print("--------------------")

for ent in doc.ents:
    if ((ent.label_ == "PER") and (" " in ent.text)):
        
        #persona mencionada
        person = ent.text
        print(person)

        print("--------------------")
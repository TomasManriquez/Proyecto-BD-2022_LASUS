import mariadb
import sys

try:
    conn = mariadb.connect(
        user="manuel",
        password="12345",
        host="localhost",
        port=3306,
        database="Proyecto_BD_SUS"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)



cur = conn.cursor()
cur.execute("show tables")

#¿Cuántas noticias fueron publicadas por cada medio de prensa?
cur.execute("SELECT a.nombre_medio, COUNT(*) FROM medio_prensa a JOIN noticias b ON a.id_medio = b.id_medio GROUP BY a.nombre_medio")

#¿Quienes son las personas mencionadas en las noticias de un día específico?
cur.execute("SELECT persona.nombre_persona FROM menciona JOIN noticias ON noticias.id_noticia = menciona.id_noticia JOIN persona ON persona.id_persona = menciona.id_persona  WHERE noticias.fecha_publicacion = '2022-06-25'")

#¿Cómo evoluciona la popularidad de una persona específica?
cur.execute("SELECT a.puntaje, a.fecha FROM popularidad a JOIN persona b ON a.id_persona = b.id_persona WHERE b.nombre_persona ='Gabriel Boric' ORDER BY fecha ")

#¿Cuáles son los 5 medios de prensa más antiguos en una región especifica?
cur.execute("SELECT nombre_medio, fecha_creacion FROM medio_prensa WHERE region ='Magallanes' ORDER BY fecha_creacion ASC LIMIT 5 ")

for row in cur:
    print(row)

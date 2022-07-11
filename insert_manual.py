import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="2610",
        host="127.0.0.1",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#se instancia la base de datos
cur.execute("USE Proyecto_BD_SUS")




#Escribir un script Python que permite insertar manualmente algunos datos en cada una de las tablas de la Base de datos.
#Entregable: insert_manual.py


#Añadir a tabla medio_prensa
cur.execute("DELETE FROM medio_prensa WHERE nombre_medio = 'El Magallanews'")
cur.execute("INSERT INTO medio_prensa(id_medio, url_medio, nombre_medio, fecha_creacion, pais, region, idioma) VALUES('000001','https://www.elmagallanews.cl/','El Magallanews','08-03-11','chile','magallanes','español')")

#Añadir a tabla noticias
cur.execute("DELETE FROM noticias WHERE id_noticia= '000001' ")
cur.execute("INSERT INTO noticias(id_noticia,url_noticia,titulo,fecha_publicacion,contenido) VALUES('000001','https://www.elmagallanews.cl/noticia/sociedad/como-afectara-mi-vida-la-nueva-constitucion','¿Cómo afectará mi vida la nueva constitución','08-07-22','Más de 40 organizaciones y académicos expertos ...')")

#Añadir a tabla dueño
cur.execute("DELETE FROM dueño WHERE  id_dueño ='000001'")
cur.execute("INSERT INTO dueño(id_dueño, nombre_dueño, persona_natural) VALUES('000001','Juanito Perez', TRUE)")

#Añadir a tabla posee
cur.execute("DELETE FROM posee WHERE  id_dueño ='000001'")
cur.execute("INSERT INTO posee( id_dueño,id_medio, fecha ) VALUES('000001','000001','08-03-11')")

#Añadir a tabla persona
cur.execute("DELETE FROM persona WHERE nombre_persona = 'hola soy german'")
cur.execute("INSERT INTO persona(id_persona, nombre_persona, url_wiki, nacionalidad, profesion, fecha_nacimiento) VALUES('000001','no menciona', 'no menciona','no menciona','no menciona','10-07-22')")

#Añadir a tabla popularidad
cur.execute("DELETE FROM popularidad WHERE id_popularidad=000001")
cur.execute("INSERT INTO popularidad(id_popularidad,puntaje,fecha) VALUES('000001','0','10-07-22')")

#Añadir a menciona tiene
cur.execute("DELETE FROM menciona WHERE id_persona = '000001'")
cur.execute("INSERT INTO menciona(id_persona, id_noticia) VALUES('1','1')")

#realiza el comit y cierra la coneccion con la base de datos

conn.commit() 
conn.close()
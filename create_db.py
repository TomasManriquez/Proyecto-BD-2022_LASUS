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

# Create Database
cur.execute("DROP database Proyecto_BD_SUS ")
query_create = "CREATE DATABASE Proyecto_BD_SUS"
cur.execute(query_create)
cur.execute("USE Proyecto_BD_SUS")

#Crea tabla dueño
cur.execute("CREATE TABLE dueño (id_dueño INT, nombre_dueño VARCHAR(32) , persona_natural BOOL, PRIMARY KEY(id_dueño))")

#Crea tabla medio_prensa
cur.execute("CREATE TABLE medio_prensa (id_medio INT, url_medio VARCHAR(300), nombre_medio VARCHAR(32), fecha_creacion DATE, pais VARCHAR(32), region VARCHAR(32), idioma VARCHAR(32), id_dueño INT, FOREIGN KEY (id_dueño) REFERENCES dueño(id_dueño), PRIMARY KEY(id_medio))")

#Crea tabla posee
cur.execute("CREATE TABLE posee (id_dueño INT, FOREIGN KEY(id_dueño) REFERENCES dueño(id_dueño), id_medio INT, FOREIGN KEY(id_medio) REFERENCES medio_prensa(id_medio), PRIMARY KEY(id_dueño, id_medio), fecha DATE)")

#Crea tabla persona
cur.execute("CREATE TABLE persona (id_persona INT, nombre_persona VARCHAR(32), url_wiki VARCHAR(300), nacionalidad VARCHAR(32), profesion VARCHAR(32), fecha_nacimiento DATE, PRIMARY KEY(id_persona))")

#Crea tabla noticia
cur.execute("CREATE TABLE noticias (id_noticia INT, url_noticia VARCHAR(300), titulo VARCHAR(128), fecha_publicacion DATE, contenido TEXT,  id_medio INT, FOREIGN KEY (id_medio) REFERENCES medio_prensa(id_medio), PRIMARY KEY(id_noticia))")

#Crea tabla menciona
cur.execute("CREATE TABLE menciona (id_persona INT, FOREIGN KEY (id_persona) REFERENCES persona(id_persona), id_noticia INT, FOREIGN KEY (id_noticia) REFERENCES noticias(id_noticia), PRIMARY KEY(id_persona, id_noticia))")

#Crea tabla popularidad
cur.execute("CREATE TABLE popularidad (id_popularidad INT, puntaje INT, fecha DATE, id_persona INT, FOREIGN KEY (id_persona) REFERENCES persona(id_persona), PRIMARY KEY(id_popularidad))")



print("Base de datos creada")

conn.commit() 
conn.close()
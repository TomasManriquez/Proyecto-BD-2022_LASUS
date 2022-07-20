import os
user = "root"
os.system(f"mysqldump -u {user} -p Proyecto_BD_SUS > Proyecto_BD_SUS_dump.sql")
print("Copia realizada con éxito.")

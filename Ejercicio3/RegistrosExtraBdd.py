import sqlite3

conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()

c.execute("INSERT INTO acciones VALUES ('25/nov/2016','venta','VTO',160,20.57)")

c.execute("INSERT INTO acciones VALUES ('26/nov/2016','compra','VTO',90,20.57)")

c.execute("INSERT INTO acciones VALUES ('27/nov/2016','compra','INV',20,15.43)")

c.execute("INSERT INTO acciones VALUES ('28/nov/2016','venta','BSA',80,10.11)")

c.execute("INSERT INTO acciones VALUES ('29/nov/2016','compra','BSA',150,10.11)")

conexion.commit()

conexion.close()

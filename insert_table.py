import sql

db = sql.DataBase("supermark.db")

db.insert("rol","nombre,descripcion","'Administrador','Administrador del sistema'")
""" db.insert("rol","nombre,descripcion","'Vendedor','Vendedor de producto'") """

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Gutierrez','Aldana','41122168','tere_gutierrez@live.com.ar','481574',1")

""" db.insert("persona","nombre,dni,direccion,telefono,email,tipo_persona",
          "'Gutierrez Aldana','41122168','Cao Guanca 10'','tere:gutierrez@','Cliente'") """

db.close()

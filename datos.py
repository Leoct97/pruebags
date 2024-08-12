import sqlite3

def obtenallproductos():
    con = sqlite3.connect("gs.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM productos;")
    resultado = res.fetchone()
    print(resultado) 
    return resultado

def insertanewproducto(id,marca,producto,fecha):
    con = sqlite3.connect("gs.db")
    cur = con.cursor()
    con.execute("insert into productos(id,marca,producto,fecha_alta) values (?,?,?,?)", (id,marca,producto,fecha))
    con.commit()
    con.close()

def actualizainventario(id,marca,inventario,fecha,producto, nuevo):
    if nuevo == 1:
        con = sqlite3.connect("gs.db")
        cur = con.cursor()
        con.execute("update inventario set inventario = ?, fecha_alta = ?  where id = ? and marca = ? and producto = ?", (inventario,fecha,id,marca,producto))
        con.commit()
        con.close
    elif nuevo == 2:
        con = sqlite3.connect("gs.db")
        cur = con.cursor()
        con.execute("insert into inventario(id,marca,inventario,producto,fecha_alta) values (?,?,?,?,?)", (id,marca,inventario,producto,fecha))
        con.commit()
        con.close()
        return 'ok'


def deleteinventario(id,marca,producto):
        con = sqlite3.connect("gs.db")
        cur = con.cursor()
        con.execute("delete from inventario where  id = ? and marca = ? and producto = ?", (id,marca,producto))
        con.commit()
        con.close()
        return 'ok'

def ventasxdia(id,marca,producto,precio,num_articulos,fecha):
        con = sqlite3.connect("gs.db")
        cur = con.cursor()
        con.execute("update inventario set inventario = ? where id = ? and marca = ? and producto = ? ", (id,marca,producto))
        con.commit()
        con.close()
        con.execute("insert into ventasaldia values (id,marca,producto,precioneto,precioxproducto,num_articulos,fecha) values (?,?,?,?,?)", (id,marca,producto,precio,num_articulos,fecha))
        return 'ok'


id = 'hola'
marca = 'hola'
inventario = 70
producto = 'hola'
fecha = 'hola'
nuevo = 1
# insertanewproducto(id,marca,producto,fecha)
# actualizainventario(id,marca,inventario,fecha,producto,nuevo)
deleteinventario(id,marca,producto)
import sqlite3
conexion = sqlite3.connect("peluqueria.db")
cursor = conexion.cursor()


def agregar_cliente():
   nombre = input("ingrese el nombre del cliente a agregar :\n")
   telefono = input ("ingrese el telefono del cliente a agregar :\n")
   while True:

      mail = input(
         "ingrese el mail del cliente a agregar :\n"
      )

      if "@gmail" in mail and ".com" in mail:
         break

      else:
         print(
            "mail invalido, debe contener @gmail y debe ser .com"
         )
   localidad = input("ingrese la localidad del cliente a agregar\n")

   cursor.execute("""
           insert into clientes(nombre,telefono,mail,localidad) values
                  (?,?,?,?)      
                   """, (nombre, telefono, mail, localidad))
   conexion.commit()
   print("cliente agregado con exito!")
   



def ver_listado_clientes():
      cursor.execute("""
          select * from clientes
      """)

      clientes = cursor.fetchall()
      if len(clientes) ==0:
          print ("lista de clientes vacia")
      else:
          for cliente in clientes:
            print (f"""
------------------- LISTA DE CLIENTES -------------- 
             ID : {cliente[0]}
             NOMBRE : {cliente[1]}
             TELEFONO : {cliente[2]}
             MAIL : {cliente[3]}
             LOCALIDAD : {cliente[4]}
----------------------------------------------------
                """)



def modificar_cliente():
 ver_listado_clientes()
 print ("INGRESE LOS DATOS DEL CLIENTE A MODIFICAR : \n")
 id_cliente = input("ingrese el id del cliente a modificar:\n")
 nombre = input("ingrese el nuevo nombre del cliente a modificar:\n")
 telefono = input("ingrese el telefono nuevo cliente a modificar:\n")
 mail = input("ingrese el nuevo mail del cliente a modificar:\n") 
 localidad = input("ingrese la nueva localidad del cliente a modificar:\n")

 cursor.execute("""
                  update clientes
                   set nombre = ?, telefono = ?, mail = ?, localidad = ? 
                   where id_cliente = ?
                   """, (nombre,telefono,mail,localidad,id_cliente))
 conexion.commit()
 print ("cliente modificado con exito!")

        



def eliminar_clientes():
 ver_listado_clientes()
 print ("ingrese el cliente a eliminar\n")
 id_cliente = input("ingrese el id del cliente a eliminar :\n")
 
 cursor.execute("""
               delete from clientes
                where id_cliente = ? 
               """, (id_cliente))
 conexion.commit()
 print ("cliente eliminado con exito!")







def menu_clientes():

    while True:

        print("""
======== Apartado de clientes ========

1 - agregar cliente
2 - ver listado de clientes
3 - modificar clientes
4 - eliminar clientes
5 - volver al menu principal              

        """)

        opcion = input("Seleccione opcion: ")



        if opcion == "1":
            agregar_cliente()
        
        elif opcion =="2":
            ver_listado_clientes()
        
        elif opcion =="3":
            modificar_cliente()
        
        elif opcion =="4":
            eliminar_clientes()
        
        elif opcion =="5":
            print("saliste del apartado de clientes")
            break;
        else:
            print ("ingrese una opcion valida dentro de nuestro menu, gracias")

            


def agregar_servicio():
 print ("ingrese los datos del servicio a agregar a continuacion \n")
 tipo_servicio = input ("indique el tipo de servicio a agregar a su turno :\n")
 
 cursor.execute("""
                insert into servicios (tipo_servicio) values 
                (?)
               """,(tipo_servicio,))
 conexion.commit()
 print("servicio agregado con exito!")



def ver_servicios():

    cursor.execute("""
    SELECT * FROM servicios
    """)

    servicios = cursor.fetchall()

    if len(servicios) == 0:
        print("lista de servicios vacia")

    else:

        for servicio in servicios:

            print(f"""
------------------- LISTA DE SERVICIOS -------------- 
ID : {servicio[0]}
TIPO DE SERVICIO : {servicio[1]}
----------------------------------------------------
""")


def modificar_servicio():

    ver_servicios()

    print("INGRESE LOS DATOS DEL SERVICIO A MODIFICAR:\n")

    id_servicio = input(
        "ingrese el id del servicio a modificar:\n"
    )

    tipo_servicio = input(
        "ingrese el nuevo servicio a modificar:\n"
    )

    cursor.execute("""
    UPDATE servicios
    SET tipo_servicio = ?
    WHERE id_servicios = ?
    """, (tipo_servicio, id_servicio))

    conexion.commit()

    print("servicio modificado con exito!")
    

def eliminar_servicio():
    ver_servicios()
    print ("ingrese el ID del servicio a eliminar \n")
    id_servicios = input("ingrese el ID del servicio a eliminar :\n")
    cursor.execute("""
                 delete from servicios 
                   where id_servicios = ?
                """,(id_servicios))
    conexion.commit()
    print ("servicio eliminado correctamente !")






def menu_servicios():

    while True:

        print("""
======== Apartado de servicios ========

1 - agregar servicio
2 - ver listado de servicios
3 - modificar servicio
4 - eliminar servicio
5 - volver al menu principal              

        """)

        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            agregar_servicio()
        
        elif opcion =="2":
            ver_servicios()
        
        elif opcion =="3":
            modificar_servicio()
        
        elif opcion =="4":
            eliminar_servicio()
        
        elif opcion =="5":
            print("saliste del apartado de servicios")
            break;
        else:
            print ("ingrese una opcion valida dentro de nuestro menu, gracias")


def agregar_turno():
    ver_listado_clientes()
    ver_servicios()
    id_cliente = input ("ingrese el ID del cliente a agregar :\n")
    id_servicios = input ("ingrese el ID del servicio a agregar :\n")
    fecha = input("ingrese la fecha a agregar a su turno :\n")
    horario = input ("ingrese el horario a agregar a su turno :\n")
    cursor.execute("""
                   select * from turnos 
                   where fecha = ?
                   and horario = ?
                   """,(fecha,horario))
    turno_existe = cursor.fetchall()
    if turno_existe:
        print ("el horario y fecha del turno, se encuentran ocupadas !")
    else:
        cursor.execute("""
                       insert into turnos(id_cliente,id_servicios,fecha,horario) values
                       (?,?,?,?)
                       """,(id_cliente,id_servicios,fecha,horario))
    try:
        conexion.commit()
        print ("turno registrado con exito !")
    except:
        print ("ocurrio un error, reviselo!")





def ver_turnos():
    cursor.execute("""
                   select 
                   turnos.id_turno,
                   clientes.nombre,
                   servicios.tipo_servicio,
                   turnos.fecha,
                   turnos.horario

                   from turnos

                   inner join clientes
                   on turnos.id_cliente = clientes.id_cliente

                   inner join servicios
                   on turnos.id_servicios = servicios.id_Servicios

                   """)
    
    turnos = cursor.fetchall()
    if (len(turnos)) == 0:
        print ("su listado de turnos se encuentra vacia !")
    else:
        for turno in turnos:
            print(f"""
             ------------ LISTADO DE TURNOS ---------------
            id_turno : {turno[0]}
            nombre de cliente : {turno[1]}
            tipo de servicio : {turno[2]}      
            fecha : {turno[3]}      
            horario : {turno[4]}
             ---------------------------------------------      
                  """)


def modificar_turno():
    ver_turnos()
    print ("los datos del turno a modificar :")
    id_turno = input ("ingrese el ID del turno a modificar :\n")
    ver_listado_clientes()
    id_cliente = input ("ingrese el ID del cliente a modificar :\n")
    ver_servicios()
    id_servicios = input ("ingrese el ID del servicio a modificar :\n")
    fecha = input ("ingrese la fecha a modificar :\n")
    horario = input ("ingrese el horario a modificar :\n")

    cursor.execute("""
                   update turnos
                   set 
                   id_cliente = ?,
                   id_servicios = ?,
                   fecha = ?,
                   horario = ?
                   where id_turno = ?
                   """,(id_cliente,id_servicios,fecha,horario,id_turno))
    conexion.commit()
    print ("turno modificado con exito!")



def eliminar_turno():
    ver_turnos()
    print ("ingrese el ID del turno a eliminar\n")
    id_turno = input("ingrese el ID del turno :\n")
    cursor.execute("""
                   delete from turnos
                   where id_turno = ?
                   """,(id_turno))
    conexion.commit()
    print ("turno modificado con exito !")




def menu_turnos():

    while True:

        print("""
======== Apartado de turnos ========

1 - agregar nuevo turno
2 - ver listado de turnos
3 - modificar turno
4 - eliminar turno
5 - volver al menu principal               

        """)

        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            agregar_turno()
        
        elif opcion =="2":
            ver_turnos()
        
        elif opcion =="3":
            modificar_turno()
        
        elif opcion =="4":
            eliminar_turno()
        
        elif opcion =="5":
            print("saliste del apartado de turnos")
            break;
        else:
            print ("ingrese una opcion valida dentro de nuestro menu, gracias")



def menu():

    while True:

        print("""
======== bienvenido al sistema de peluqueria ========

1 - clientes
2 - servicios
3 - turnos
4 - salir

        """)

        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            menu_clientes()
        
        elif opcion =="2":
            menu_servicios()
        
        elif opcion =="3":
            menu_turnos()
        
        elif opcion =="4":
            print("saliste del sistema, que tenga buen dia")
            break;
        else:
            print ("ingrese una opcion valida dentro de nuestro menu, gracias")


menu()





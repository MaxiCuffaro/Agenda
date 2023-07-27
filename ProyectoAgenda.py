def menu():
 print ( """" 
*** menu de la agenda ***
    1 )Anotar datos de contactos
    2) Mostrar datos de contactos
    0) salir
""")
menu()

opcion = -1
directorio=[]

def agregarcontacto ():
    nombre = input(" ingrese el nombre de contacto")
    telefono = input(" ingrese el cel de su contacto")
    direccion = input(" ingrese la dire de su contacto")
    directorio.append([nombre, telefono, direccion])
    print("se agrego correctamente el contacto")

def mostrarcontacto ():
    print("esta es la lista de contactos : ")
    if not directorio :
        print ("su agenda esta vacia")
    else:
        print ("esta es su lista de contactos:")
    for contacto in directorio:
        print(" datos del contacto:",contacto )

def despedida ():
    print("gracias por usar nuestra agenda ")

def pediropcioncorrecta ():    
    print("ingrese opcion correcta")

while opcion != 0:
    menu()
    opcion= int (input("inserte la opcion que desea realizar: "))
    
    if opcion == 1:
        agregarcontacto()

    elif opcion == 2:
        mostrarcontacto()

    elif opcion == 0: 
        despedida()
else :
    pediropcioncorrecta()

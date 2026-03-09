class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# Clase Lista enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacía
    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
        else:
            print("Lista no vacía")

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    # Contador
    def contador(self):
        contador = 0
        nodoesp = self.cabeza
        while nodoesp is not None:
            contador += 1
            nodoesp = nodoesp.siguiente
        return contador

    # Buscar un elemento
    def buscador(self, data):
        nodoesp = self.cabeza
        while nodoesp is not None:
            if nodoesp.data == data:
                return True
            nodoesp = nodoesp.siguiente
        return False
    
    #Buscador posicion
    def buscapos(self,data):
        nodoesp=self.cabeza
        pos=0
        while nodoesp.data is not None:
            if nodoesp.data==data:
                return pos
            nodoesp=nodoesp.siguiente
            pos+=1

    # Imprimir Lista
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente

    #Vaciar
    def vaciar(self):
        self.cabeza=None

    #Huespedes
    def huespedes(self,data):
        print("Seleccione una opcion")
        opc=input(int(f"1. Consulta de huespedes, /n, 2. Consulta de habitaciones"))
        if opc==1:
            opc2=input(int(f"1. Individual, /n, 2. Total"))
            if opc2==1:
                nombre=str(input("Ingrese el nombre del cliente: "))
                if self.buscador(nombre):
                    print(f"El cliente {nombre} esta hospedado")
                else:
                    print("El cliente no existe")
            elif opc2==2:
                opc3=int(input(f"1. Por cedula, 2. Por orden de llegada"))
                if opc3==1:
                    self.buscador(data)
                    print(f"El cliente {data} tiene {self.contador()} huespedes")
                elif opc3==2:
                    self.buscador(data)
                    print(f"El cliente {data} ")
                print("El total de huespedes es: ",self.contador())
            else:
                print("Opcion no valida")
        elif opc==2:
            opc4=int(input(f"1. Lista de habitaciones disponibles, /n, 2. Lista de habitaciones ocupadas"))
            if opc4==1:
                print("El total de habitaciones disponibles es: ",self.contador())
            elif opc4==2:
                print("El total de habitaciones ocupadas es: ",self.contador())
        else:
            print("Opcion no valida")

listaH1=ListaSE()
listaH2=ListaSE()
listaH3=ListaSE()
listaH4=ListaSE()
listaH5=ListaSE()

Opc=0
while Opc!=6:
    print("Seleccione una opcion")
    Opc=int(input(f"1. Agregar huespedes, 2. Quitar huespedes, 3. Consultar huespedes, 4. Quitar habitaciones, 5. Consultar habitaciones, 6. Salir: "))
    if Opc==1:
        centi=1
        while centi!=2:
            Nhab=int(input("En que habitacion se va a hospedar?: "))
            if Nhab==1:
                ced=int(input("Ingrese el numero de cedula: "))
                listaH1.agregarInicio(ced)
                nom=str(input("Ingrese el nombre del cliente: "))
                listaH1.agregarInicio(nom)
                listaH1.agregarInicio(Nhab)
            elif Nhab==2:
                ced=int(input("Ingrese el numero de cedula: "))
                listaH2.agregarInicio(ced)
                nom=str(input("Ingrese el nombre del cliente: "))
                listaH2.agregarInicio(nom)
                listaH2.agregarInicio(Nhab)
            elif Nhab==3:
                ced=int(input("Ingrese el numero de cedula: "))
                listaH3.agregarInicio(ced)
                nom=str(input("Ingrese el nombre del cliente: "))
                listaH3.agregarInicio(nom)
                listaH3.agregarInicio(Nhab)
            elif Nhab==4:
                ced=int(input("Ingrese el numero de cedula: "))
                listaH4.agregarInicio(ced)
                nom=str(input("Ingrese el nombre del cliente: "))
                listaH4.agregarInicio(nom)
                listaH4.agregarInicio(Nhab)
            elif Nhab==5:
                ced=int(input("Ingrese el numero de cedula: "))
                listaH5.agregarInicio(ced)
                nom=str(input("Ingrese el nombre del cliente: "))
                listaH5.agregarInicio(nom)
                listaH5.agregarInicio(Nhab)
            else:
                print("Habitacion no encontrada")
            centi=int(input("1. Continuar, 2. Salir: "))
        print("Habitacion 1")
        listaH1.imprimir()
        print("Habitacion 2")
        listaH2.imprimir()
        print("Habitacion 3")
        listaH3.imprimir()
        print("Habitacion 4")
        listaH4.imprimir()
        print("Habitacion 5")
        listaH5.imprimir()
    elif Opc==2:
        qui=int(input("Ingrese la cedula del huesped que desea quitar: "))
        print(f"La posicion del huesped en la lista es de {lista.buscapos(qui)}")
        lista.eliminaresph(qui)
    elif Opc==3:
        Nhab=int(input("Que habitacion quiere consultar?: "))
        if Nhab==1:
            listaH1.huespedes()
        elif Nhab==2:
            listaH2.huespedes()
        elif Nhab==3:
            listaH3.huespedes()
        elif Nhab==4:
            listaH4.huespedes()
        elif Nhab==5:
            listaH5.huespedes()
        else:
            print("Habitacion no encontrada")
    elif Opc==4:
        qui=int(input("Ingrese la habitacion que desea quitar: "))
        if qui==1:
            listaH1.vaciar()
        elif qui==2:
            listaH2.vaciar()
        elif qui==3:
            listaH3.vaciar()
        elif qui==4:
            listaH4.vaciar()
        elif qui==5:
            listaH5.vaciar()
        else:
            print("Habitacion no encontrada")
    elif Opc==5:
        lista.huespedes()

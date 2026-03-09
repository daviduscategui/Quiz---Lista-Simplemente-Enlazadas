class Nodo:
    def __init__(self, data, prioridad=0):
        self.data = data
        self.siguiente = None
        self.prioridad=prioridad

# Clase Lista enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacía
    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
            return True
        else:
            print("Lista no vacía")
            return False

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    #Agregar orden de llegada
    def agregar(self,data,prioridad):
        nuevoNodo=Nodo(data,prioridad)
        if self.cabeza is None:
            self.cabeza=nuevoNodo
            return
        elif nuevoNodo.prioridad<=self.cabeza.prioridad:
            nuevoNodo.siguiente=self.cabeza
            self.cabeza=nuevoNodo
            return
        actual=self.cabeza
        while actual.siguiente is not None and actual.siguiente.prioridad<=prioridad:
            actual=actual.siguiente
        nuevoNodo.siguiente = actual.siguiente
        actual.siguiente = nuevoNodo

    # Contador
    def contador(self):
        contador = 0
        nodoesp = self.cabeza
        while nodoesp is not None:
            contador += 1
            nodoesp = nodoesp.siguiente
        return contador
    
    #Buscador en listas
    def buscalist(self,listas,x):
        for i, lista in enumerate(listas):
            nodoesp=lista.cabeza
            while nodoesp is not None:
                if nodoesp.data==x:
                    print(f"Encontrado en lista {i}")
                    return i
                nodoesp=nodoesp.siguiente
        print("No encontrado en ninguna lista")
        return None

    # Imprimir Lista
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.siguiente

    #Vaciar
    def vaciar(self):
        self.cabeza=None

listaH1=ListaSE()
listaH2=ListaSE()
listaH3=ListaSE()
listaH4=ListaSE()
listaH5=ListaSE()
listaO=ListaSE()

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
                nom=str(input("Ingrese el nombre del cliente: "))
                hora=float(input("Ingrese la hora de su llegada: "))
                dia=int(input("Ingrese el dia de su llegada: "))
                listaH1.agregarInicio((ced, nom, Nhab, hora))
                listaO.agregar((ced, nom, Nhab, hora), dia)
            elif Nhab==2:
                ced=int(input("Ingrese el numero de cedula: "))
                nom=str(input("Ingrese el nombre del cliente: "))
                hora=float(input("Ingrese la hora de su llegada: "))
                dia=int(input("Ingrese el dia de su llegada: "))
                listaH2.agregarInicio((ced, nom, Nhab, hora))
                listaO.agregar((ced, nom, Nhab, hora), dia)
            elif Nhab==3:
                ced=int(input("Ingrese el numero de cedula: "))
                nom=str(input("Ingrese el nombre del cliente: "))
                hora=float(input("Ingrese la hora de su llegada: "))
                dia=int(input("Ingrese el dia de su llegada: "))
                listaH3.agregarInicio((ced, nom, Nhab, hora))
                listaO.agregar((ced, nom, Nhab, hora), dia)
            elif Nhab==4:
                ced=int(input("Ingrese el numero de cedula: "))
                nom=str(input("Ingrese el nombre del cliente: "))
                hora=float(input("Ingrese la hora de su llegada: "))
                dia=int(input("Ingrese el dia de su llegada: "))
                listaH4.agregarInicio((ced, nom, Nhab, hora))
                listaO.agregar((ced, nom, Nhab, hora), dia)
            elif Nhab==5:
                ced=int(input("Ingrese el numero de cedula: "))
                nom=str(input("Ingrese el nombre del cliente: "))
                hora=float(input("Ingrese la hora de su llegada: "))
                dia=int(input("Ingrese el dia de su llegada: "))
                listaH5.agregarInicio((ced, nom, Nhab, hora))
                listaO.agregar((ced, nom, Nhab, hora), dia)
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
        nomb=str(input("Ingrese el nombre: "))
        listas=[listaH1,listaH2,listaH3,listaH4,listaH5]
        habitacion=listaH1.buscalist(listas,nomb)
        if habitacion is None:
            print(f"Cliente {nomb} no encontrado")
        elif habitacion==0:
            listaH1.vaciar()
        elif habitacion==1:
            listaH2.vaciar()
        elif habitacion==2:
            listaH3.vaciar()
        elif habitacion==3:
            listaH4.vaciar()
        elif habitacion==4:
            listaH5.vaciar()
    elif Opc==3:
        print("Seleccione una opcion")
        opc=int(input(f"1. Individual, 2. Total: "))
        listas=[listaH1,listaH2,listaH3,listaH4,listaH5]
        if opc==1:
            nomb=str(input("Ingrese el nombre: "))
            habitacion=listaH1.buscalist(listas,nomb)
            if habitacion is not None:
                print(f"El cliente {nomb} esta hospedado en la habitacion {habitacion+1}")
            else:
                print(f"Cliente {nomb} no encontrado")
        elif opc==2:
            opc3=int(input("1. Por cedula, 2. Por orden de llegada: "))
            if opc3==1:
                ced=int(input("Ingrese la cedula: "))
                habitacion=listaH1.buscalist(listas,ced)
                if habitacion is not None:
                    print(f"El cliente {ced} esta hospedado en la habitacion {habitacion+1}")
                else:
                    print(f"Cliente {ced} no encontrado")
            elif opc3==2:
                listaO.imprimir()
            else:
                print("Opcion invalida")
        else:
            print("Opcion invalida")
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
        print("Seleccione una opcion")
        opc4=int(input(f"1. Lista de habitaciones disponibles, 2. Lista de habitaciones ocupadas: "))
        if opc4==2:
            contd=0
            if listaH1.vacio() is False:
                contd+=1
                print("Habitacion 1")
                listaH1.imprimir()
            if listaH2.vacio() is False:
                contd+=1
                print("Habitacion 2")
                listaH2.imprimir()
            if listaH3.vacio() is False:
                contd+=1
                print("Habitacion 3")
                listaH3.imprimir()
            if listaH4.vacio() is False:
                contd+=1
                print("Habitacion 4")
                listaH4.imprimir()
            if listaH5.vacio() is False:
                contd+=1
                print("Habitacion 5")
                listaH5.imprimir()
            print(f"Hay {contd} habitaciones ocupadas")
        elif opc4==1:
            conto=0
            if listaH1.vacio() is True:
                conto+=1
                print("Habitacion 1")
                listaH1.imprimir()
            if listaH2.vacio() is True:
                conto+=1
                print("Habitacion 2")
                listaH2.imprimir()
            if listaH3.vacio() is True:
                conto+=1
                print("Habitacion 3")
                listaH3.imprimir()
            if listaH4.vacio() is True:
                conto+=1
                print("Habitacion 4")
                listaH4.imprimir()
            if listaH5.vacio() is True:
                conto+=1
                print("Habitacion 5")
                listaH5.imprimir()
            print(f"Hay {conto} habitaciones disponibles")
        else:
            print("Opcion invalida")

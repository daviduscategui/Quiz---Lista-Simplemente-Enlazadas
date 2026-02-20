class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
       
    #Contador 
		contador=0
		def contador(self):
			if self.cabeza==None:
				return 0
			else:
				nodoesp=self.cabeza
				while nodoesp!=None:
					contador+=1
					nodoesp=nodoesp.siguiente
					return contador

	# Eliminar nodo index
	def eliminar_index(self, index):
		if self.cabeza == None:
			return
		nodo_actual = self.cabeza
		posicion = 0
		if posicion == index:
			self.eliminarInicio()
		else:
			while(nodo_actual != None and posicion+1 != index):
				posicion = posicion+1
				nodo_actual = nodo_actual.siguiente
			if nodo_actual != None:
				nodo_actual.siguiente = nodo_actual.siguiente.siguiente
			else:
				print("Nodo no encontrado")

    #Buscar un elemento
	def buscador(self,data):
		cent=input(int("Ingrese el elemento a buscar: "))
		if self.cabeza==None:
			return False
		else:
			nodoesp=self.cabeza
			while nodoesp!=cent:
				nodoesp=nodoesp.siguiente
				if nodoesp==None:
					return False
      
	# Imprimir Lista
	def imprimir(self):
		nodo_actual = self.cabeza
		while(nodo_actual):
			print(nodo_actual.data)
			nodo_actual = nodo_actual.siguiente

#Huespedes
def huespedes(self,data):
        print("Seleccione una opcion")
        opc=input(int(f"1. Consulta de huespedes, /n, 2. Consulta de habitaciones"))
        if opc==1:
            opc2=input(int(f"1. Individual, /n, 2. Total"))
            if opc2==1:
                print("Ingrese el nombre del cliente")
                nombre=input()
                if self.buscador(nombre):
                    print(f"El cliente {nombre} tiene {self.contador()} huespedes")
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
            
lista = ListaSE()

Opc=0
while Opc!=6:
    print("Seleccione una opcion")
    Opc=int(input(f"1. Agregar huespedes, 2. Quitar huespedes, 3. Consultar huespedes, 4. Quitar habitaciones, 5. Consultar habitaciones, 6. Salir "))
    if Opc==1:
        nom=str(input("Ingrese el nombre del cliente: "))
        lista.agregarInicio(nom)
        ced=int(input("Ingrese el numero de cedula: "))
        lista.agregarInicio(ced)
        lista.imprimir()
    elif Opc==2:
        qui=int(input("Ingrese la cedula del huesped que desea quitar: "))
        lista.eliminar_index(qui)
        lista.imprimir()
    elif Opc==3:
        lista.huespedes()
    elif Opc==4:
        print("VA")
    
lista.agregarInicio(10)
lista.agregarInicio(20)
print(lista.vacio())
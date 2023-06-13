#Ejercicicio 3*: Implementar la clase cola vista en clase
class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""

    def __init__(self, elementos= []) -> None:
        self.elementos = elementos
        

    def agregar(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool: 
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)

    def imprimir(self):
        for i in self.elementos:
            return i

    def vaciar(self):
        return self.elementos.clear()

    def __str__(self):
        return ("{}".format(self.elementos))

    def __eq__ (self,otro_elementos):
        return (self.elementos == otro_elementos.elementos)

p = Cola() # crea una cola (vacia)
print(p.es_vacia()) #True
assert p.es_vacia() == True

p.agregar(4) # 
p.agregar('perro')
print(p.elementos) # [4,'perro']
print(p.primero()) # 4
assert p.primero() == 4

p.agregar(True) # [4,'perro',true]
print(p.tamanio()) # 3
assert p.tamanio() == 3

print(p.es_vacia()) #False
assert p.es_vacia() == False
p.agregar(8.4) # [4,'perro',true,8.4]

print(p.sacar()) # imprime el 4 y lo saca
print(p.sacar()) # impreme perro y lo saca
print(p.tamanio()) # 2
assert p.tamanio() == 2
assert p.primero() == True

#Ejercicio 4 *
""" Modificar el init para que la cola pueda empezar con una lista
"""

cola = Cola([1,2,3,4])
atender = cola.sacar()
print(atender) # 1
assert atender == 1

#Ejercicio 5
""" Agregar a la clase cola un método:
    - Imprimir uno a uno los elementos de la cola
"""
cola = Cola([1,2,3,4])
cola.imprimir()

#Ejercicio 6*
""" Agregar a la clase cola un método:
    - Vaciar la cola
"""

cola = Cola([1,2,3,4])
assert cola.es_vacia == False
cola.vaciar()
assert cola.es_vacia == True

#Ejercicio 7*
def revertir_str(palabra)->str:
    """ toma un string y devuelve las palabras en sentido inverso """
    palabra.reverse()

palabra = "Python"
reverse = revertir_str(palabra)
print(reverse)
assert reverse == "nohtyP"

#Ejercicio 7. a *
""" Agregar a la clase cola un método:
    - __eq__ que dice si dos colas son iguales
"""
cola1 = Cola([1,2,3,4])
cola2 = Cola([1,2,3,4])
assert cola1 == cola2
cola3 = Cola([1,2,3,2])
assert cola1 != cola2

# Ejercicio 8:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2, manteniendo
#  el orden de salida de los elementos. Al finalizar la Cola C1 no debe contener elementos.
"""
def trasladar_p(c:cola)->cola:
    pass
c2 = trasladar(c1)
assert c1.es_vacia == True
"""
# Ejercicio 9:
"""
409 Diseña un método copia que devuelva una nueva Cola cuyo contenido es el mismo
de la Cola sobre la que se invoca el método. ¡Ojo con la memoria cuando saques una copia de
self cola!
"""
"""
    def copiar_p(self:Cola)->Cola:
        pass
c2 = c1.copiar_p(c1)
c1 == c2
assert c1.es_vacia == True
"""
# Ejercicio 10 *
""" Escriba un metodo de Cola que dada una cola C1 reciba una cola C2  de 
números enteros y devuelva una nueva Cola con los elementos concatenados en el 
orden C1 y C2. Es de destacar que las Colas recibidas no deben sufrir ningún 
tipo de cambio o alteración.(en principio utilizar los métodos de cola para la 
tarea)"""

def concat(C1:cola,C2:cola)->Cola:
    cola_nueva=Cola()
    
    while not C1.es_vacia():
        elem = C1.sacar()
        cola_nueva.agregar(elem)
        C1.agregar(elem)
        
    while not C2.es_vacia():
        elem = C2.sacar()
        cola_nueva.agregar(elem)
        C2.agregar(elem)
    return cola_nueva


C1=Cola()
C2=Cola()
C1.agregar(1)
C1.agregar(4)
C1.agregar(8)
C2.agregar(4)
C1.agregar(2)
C1.agregar(7)
print(C1)
print(C2)
res = concat(C1,C2)  #devuelve una cola [1,4,8,4,2,7] c1 sigue siendo [1,4,8]
print (res)

# Ejercicio 11 *
"""
410
Diseña un programa que gestiona una lista de espera de pacientes usando la clase
Cola definida en este apartado. Cada paciente tiene un nombre y un número de la seguridad
El programa presentará un menú con las siguientes opciones: 1) añadir un paciente a la
lista de espera; 2) atender al primer paciente de la lista; y 3) finalizar la ejecución del programa.
Al seleccionar un paciente se solicitarán los datos del paciente y se añadirá este a la lista de
espera (que es una cola). Al seleccionar la segunda opción, aparecerá en pantalla el nombre del
paciente y se eliminará a este de la cola. La lista de espera respetará estrictamente el orden de
llegada de los pacientes.
"""

opcion=0
turno=0
pacientes= Cola()
while opcion != "3":
    opcion= int(input("\n1 Agregar un paciente a la lista de espera, \n2 Atender al primer paciente de la lista \n3 Finalizar la ejecución del programa:    \n"))
    if opcion=="1":
        paciente=input("Ingrese el nombre del paciente: ")
        dni=input("Ingrese el número de DNI del paciente: ")
        turno +=1
        paciente= (paciente, dni, turno)
        pacientes.agregar(paciente)
        print(f"El paciente {paciente[0]} con DNI {paciente[1]}, turno{paciente[2]} ha sido agregado a la lista de espera.")
        print("Lista de pacientes en espera: ", pacientes)
    
    elif opcion == "2":
        if not pacientes.estaVacia():
            paciente= pacientes.sacar()
            print(f"El paciente {paciente[0]} con DNI {paciente[1]} y turno {paciente[2]} ha sido atendido.")
        else:
            print("No hay pacientes en espera.")   

    elif opcion == "3":
        break    

# Ejercicio 12 
"""
Modifique el programa anterior para que acepte hacer cola para 3 especialidades
- Radiografia
- Clínico
- Analisis

Cuando ingrese un paciente nuevo deberá indicar para que especilidad desea el turno
Cuando atienda un paciente deberá decir de que especialidad desea atender
"""
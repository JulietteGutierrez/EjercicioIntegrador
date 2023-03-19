#Ejercicio Integrador para el curso DJANGO 2023
#Autor: Julieta Gutierrez

class Persona:
    def __init__(self,nombre=None,edad=None,DNI=None):
        #if nombre != None:
        self.__nombre = nombre
        #if edad != None:
        self.__edad = edad
        #if  != None:
        self.__DNI = DNI
    
    #GETTER
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    #SETTER
    @nombre.setter
    def nombre(self,nombre):
        assert type(nombre) is str, "El nombre debe ser una cadena de texto"
        self.__nombre = nombre

    @edad.setter
    def edad(self,edad):
        assert type(edad) is int, "La edad debe ser un numero entero"
        self.__edad = edad

    @DNI.setter
    def DNI(self,DNI):
        assert type(DNI) is int, "El DNI debe ser un numero entero sin puntos"
        self.__DNI = DNI

    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} anios y DNI n {self.DNI} ")

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta:
    def __init__(self,titular,cantidad=None):
        self.__titular = titular
        self.__cantidad = cantidad
    
    #GETTER
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    #SETTER
    @titular.setter
    def titular(self,titular):
        assert type(titular) is Persona, "El titular debe ser una Persona"
        self.__titular = titular

    def mostrar(self):
        print(f"El titular de la cuenta es: {self.__titular.nombre}, DNI {self.__titular.DNI} y tiene {self.__cantidad} pesos en la misma. ")

    def ingresar(self,dinero):
        if dinero > 0:
            self.cantidad += dinero

    def retirar(self,dinero):
        self.cantidad -= dinero

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    #GETTER
    @property
    def bonificacion(self):
        return self.__bonificacion

    #SETTER
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return self.titular.edad <= 25 and self.titular.edad >= 18

    def retirar(self,dinero):
        if es_titular_valido(self):
            self.cantidad -= dinero
        else:
            print(f"{juli.nombre} No es un titular valido  y no puede retirar dinero ")

    def mostrar(self):
        print(f"Cuenta Joven")
        print(f"bonificacion: {self.__bonificacion} %.")

juli = Persona(nombre = "Julieta")
juli.nombre = "Julieta Gutierrez"
juli.edad = 32
juli.DNI = 35620435

juli.mostrar()

if juli.es_mayor_de_edad():
    print(f"{juli.nombre} tiene {juli.edad} anios y es mayor de edad ")
else:
    print(f"{juli.nombre} tiene {juli.edad} anios y NO es mayor de edad ")

micuenta = Cuenta(juli,20)
micuenta.mostrar()

micuenta2 = CuentaJoven(juli,20,10)
micuenta2.mostrar()
if micuenta2.es_titular_valido():
    print(f"{micuenta2.titular.nombre} es un titular valido")
else:
    print(f"{micuenta2.titular.nombre} NO es un titular valido")

"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod,n1,n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_n1(self , n1):

        self.nota1 = n1

    def obtener_n1(self):

        return self.nota1

    def agregar_n2(self , n2):

        self.nota2 = n2

    def obtener_n2(self):

        return self.nota2

    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo , self.nota1, self.nota2)


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado

        
    def obtener_promedio_n1(self):
        print ("El promedio de la nota 1 es :")
        suma = 0 
        for n in self.listado_personas:
            suma = suma + n.obtener_n1()

        prom = suma/len(self.listado_personas)

        return prom

    def obtener_promedio_n2(self):
        print ("El promedio de la nota 2 es :")
        suma=0
        for n in self.listado_personas:
            suma = suma + n.obtener_n2()

        prom = suma/len(self.listado_personas)

        return prom


    def obtener_listado_n1(self):
        print ("Las personas que tienen la nota 1 menor a 15 son  ")
        for n in self.listado_personas:
            if (n.obtener_n1() < 15):
                menor = "%s - %s - %d \n" %(n.obtener_nombre(), n.obtener_apellido(), n.obtener_n1())
        return menor

    def obtener_listado_n2(self):
        print ("Las personas que tienen la nota 2 menor a 15 son  ")
        for n in self.listado_personas:
            if (n.obtener_n2() < 15):
                menor = "%s - %s - %d \n" %(n.obtener_nombre(), n.obtener_apellido(), n.obtener_n2())
        return menor

    def obtener_listado_personas(self):
        print ("Las personas que su nombre inicia con la latra R y J son ")
        nombre = ""
        for n in self.listado_personas:
            if (n.obtener_nombre()[0:1] == "R" or n.obtener_nombre()[0:1] == "J" ):
                nombre= "%s%s %s \n"%(nombre,n.obtener_nombre() , n.obtener_apellido())
        return nombre
                


    def __str__(self):
        cadena = "" 
        for n in self.listado_personas:
            cadena = "%s %s %s \n  " % (cadena, n.obtener_nombre(), \
                n.obtener_apellido())
        return cadena     



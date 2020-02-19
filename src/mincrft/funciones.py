import json, sys

archivo=json.load(open('/usr/mincrft/minecraft.json'))
	
class Funciones(object):
    switcher={
        "todosDirectorio":0,
        "directorio":1
    } 
    def __init__(self, argument):
        method = getattr(self, str(argument[1]), lambda: "Opcion invalida")
        if self.switcher.get(argument[1]) >= 1:
            return method(argument) 
        else:
            return method()

    def todosDirectorio(self):
        for juegos in archivo['juegos']:
            print (juegos['id']+ "")
    
    def directorio(self,juego):
        existe=False
        for juegos in archivo['juegos']:
            if juegos['id'] == juego[2] : 
                directorio=archivo['directorio_principal'] +juegos['directorio']+ ""
                existe=True
                break
        if existe == False:
            print ("Error")
        elif existe == True:
            print (directorio)

Funciones(sys.argv)
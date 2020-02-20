import json, sys

nombre_archivo='/usr/mincrft/minecraft.json'
archivo=json.load(open(nombre_archivo))
	
class Minecraft(object):
    switcher={
        "todosDirectorio":0,
        "directorio":1,
        "log":1

    } 
    mensajes={
        "directorio":"Error",
        "nojuegos":"Error",
        "log":"Error"
    } 

    def __init__(self, argument):
        method = getattr(self, str(argument[1]), lambda: "Opcion invalida")
        if self.switcher.get(argument[1]) >= 1:
            return method(argument) 
        else:
            return method()

    def todosDirectorio(self):
        juegos=""
        for juego in archivo['juegos']:
            juegos=juegos+juego['id']+ "/  "
        if juegos != "":
            print (juegos)
        else:
            print (self.mensajes.get('nojuegos'))
    
    def directorio(self,juego):
        directorio=""
        for juegos in archivo['juegos']:
            if juegos['id'] == juego[2] : 
                directorio=archivo['directorio_principal'] +juegos['directorio']
                break

        if directorio != "" :
            print (directorio)
        elif directorio == "":
            print (self.mensajes.get('directorio'))
    
    def log(self,juego):
        log=""
        for juegos in archivo['juegos']:
            if juegos['id'] == juego[2] : 
                log=archivo['directorio_principal'] +juegos['directorio']+juegos['log']
                break
        if log != "" :
            print (log)
        elif log == "":
            print (self.mensajes.get('log'))

Minecraft(sys.argv)
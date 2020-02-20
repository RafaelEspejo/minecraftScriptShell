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
        for juego in archivo.get('juegos'):
            juegos=juegos+juego.get('id')+ "/  "
        if juegos != "":
            print (juegos)
        else:
            print (self.mensajes.get('nojuegos'))
    
    def directorio(self,juego):
        directorio=""
        for juegos in archivo.get('juegos'):
            if juegos.get('id') == juego[2] : 
                directorio=archivo.get('directorio_principal') +juegos.get('directorio')
                break

        if directorio != "" :
            print (directorio)
        elif directorio == "":
            print (self.mensajes.get('directorio'))
    
    def log(self,juego):
        log=""
        for juegos in archivo.get('juegos'):
            if juegos.get('id') == juego[2] : 
                log=archivo.get('directorio_principal') +juegos.get('directorio')+juegos.get('log')
                break
        if log != "" :
            print (log)
        elif log == "":
            print (self.mensajes.get('log'))

    def salvar(self,juego):
        pass
Minecraft(sys.argv)
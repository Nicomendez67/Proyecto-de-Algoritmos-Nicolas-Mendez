from Experimentos import Experimento


class Gestion_experimentos():
    
    def crear_experimento(labo, experimentos_json):
        experimento_objetos=[]
        for experimento in experimentos_json:
            experimento_objetos.append(Experimento(experimento["id"],experimento["receta_id"],experimento["personas_responsables"],experimento["fecha"],experimento["costo_asociado"],experimento["resultado"]))
        labo.experimento=experimento_objetos
        return experimento_objetos
    

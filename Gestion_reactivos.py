from Reactivos import Reactivo

class Gestion_reactivos():

    def crear_reactivos(labo,reactivos_json):
        reactivos_objetos=[]
        for reactivo in reactivos_json:
            reactivos_objetos.append(Reactivo(reactivo["id"],reactivo["nombre"],reactivo["descripcion"],reactivo["costo"],reactivo["categoria"],reactivo["inventario_disponible"],reactivo["unidad_medida"],reactivo["fecha_caducidad"],reactivo["minimo_sugerido"],reactivo["conversiones_posibles"]))
        labo.reactivos=reactivos_objetos
        return reactivos_objetos

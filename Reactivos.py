import json
import datetime

class Reactivo:
    def __init__(self, nombre, descripcion, costo, categoria, inventario, unidad_medida, fecha_caducidad=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.categoria = categoria
        self.inventario = inventario
        self.unidad_medida = unidad_medida
        self.fecha_caducidad = fecha_caducidad

    def actualizar_inventario(self, cantidad):
        self.inventario += cantidad

    def cambiar_unidad_medida(self, nueva_unidad):
        self.unidad_medida = nueva_unidad

    def esta_caducado(self):
        if self.fecha_caducidad:
            return datetime.datetime.strptime(self.fecha_caducidad, '%Y-%m-%d').date() < datetime.date.today()
        return False

class GestionReactivos:
    def __init__(self, archivo_datos='datos.json'):
        self.reactivos = self.cargar_datos(archivo_datos)

    def cargar_datos(self, archivo_datos):
        try:
            with open(archivo_datos, 'r') as f:
                datos = json.load(f)
            return [Reactivo(**r) for r in datos.get('reactivos', [])]
        except FileNotFoundError:
            return []

    def guardar_datos(self, archivo_datos='datos.json'):
        datos = {'reactivos': [r.__dict__ for r in self.reactivos]}
        with open(archivo_datos, 'w') as f:
            json.dump(datos, f, indent=4)

    def agregar_reactivo(self, reactivo):
        self.reactivos.append(reactivo)
        self.guardar_datos()

    def eliminar_reactivo(self, nombre):
        self.reactivos = [r for r in self.reactivos if r.nombre != nombre]
        self.guardar_datos()

    def editar_reactivo(self, nombre, nuevos_datos):
        for reactivo in self.reactivos:
            if reactivo.nombre == nombre:
                for clave, valor in nuevos_datos.items():
                    setattr(reactivo, clave, valor)
        self.guardar_datos()

    def verificar_inventario_minimo(self, minimo):
        for reactivo in self.reactivos:
            if reactivo.inventario < minimo:
                print(f"¡Advertencia! El reactivo {reactivo.nombre} está por debajo del mínimo.")
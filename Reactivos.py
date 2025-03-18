
import datetime

class Reactivo:
    def __init__(self,id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida,fecha_caducidad,minimo_sugerido,conversiones_posibles):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.costo=costo
        self.categoria=categoria
        self.inventario_disponible=inventario_disponible
        self.unidad_medida=unidad_medida
        self.fecha_caducidad=fecha_caducidad
        self.minimo_sugerido=minimo_sugerido
        self.conversiones_posibles=conversiones_posibles
        
    
    def show_attr(self):
        atributos = [
            f"Atributos del Reactivo:",
            f"ID: {self.id}",
            f"Nombre: {self.nombre}",
            f"Descripción: {self.descripcion}",
            f"Costo: {self.costo}",
            f"Categoría: {self.categoria}",
            f"Inventario Disponible: {self.inventario_disponible}",
            f"Unidad de Medida: {self.unidad_medida}",
            f"Fecha de Caducidad: {self.fecha_caducidad}",
            f"Mínimo Sugerido: {self.minimo_sugerido}",
        "Conversiones posibles:"
    ]

        for i in self.conversiones_posibles:
            for unidad, factor in i.items():
                atributos.append(f"{unidad}: {factor}")
    
        return "\n".join(atributos)

    def crear_reactivos(lista_r):
        
        id = len(lista_r)+1
        nombre = input("Nombre del nuevo reactivo: ")
        descripcion = input("Descripcion del nuevo reactivo: ")
        costo = float(input("Costo del nuevo reactivo: "))
        categoria = input("Categoria del nuevo reactivo: ")
        inventario_disponible = int(input("Cantidad de inventario que posee el nuevo reactivo: "))
        unidad_medida = input("Unidad de medida del nuevo reactivo: ")
        fecha_caducidad = int(input("Fecha de caducidad del nuevo reactivo: "))
        minimo_sugerido = float(input("Minimo sugerido del nuevo reactivo: "))
        conversiones = int(input("Número de conversiones posibles del nuevo reactivo: "))
        conversiones_posibles = []
        for _ in range(conversiones):
            unidad = input("Unidad de medida del nuevo reactivo: ")
            factor = float(input("Factor de conversion del nuevo reactivo: ")) 
            conversiones_posibles.append((unidad, factor))
      
        reactivo_nuevo = Reactivo(id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida, fecha_caducidad, minimo_sugerido, conversiones_posibles)
        lista_r.append(reactivo_nuevo)
        return reactivo_nuevo, lista_r
    
    def editar(self, nombre, atributo, nuevo_valor):

        nombre = input("Nombre del reactivo a editar: ")
        atributo = input("Atributo del reactivo a editar: ")
        nuevo_valor = input("Valor nuevo del atributo: ")
        for reactivo in self.reactivos:
            if reactivo.nombre == nombre:
                if hasattr(reactivo, atributo):
                    setattr(reactivo, atributo, nuevo_valor)
                    print(f'Atributo "{atributo}" del reactivo "{nombre}" actualizado a "{nuevo_valor}"')
                else:
                    print(f'El atributo "{atributo}" no existe en el reactivo "{nombre}"')
                return
        print(f'No hay reactivo con el nombre "{nombre}"')

        for reactivo in self.reactivos:
            if reactivo.id == id:
                reactivo.editar_atributo(atributo, nuevo_valor)
                return
            print(f'No se encontró un reactivo con id: {id}')

    def eliminar(self, lista_r):
     
        eliminar = input(f"¿Eliminar el reactivo {self.nombre}? \n1-si \n2-no ")
        if eliminar == "1":
            lista_r.remove(self)
            print(f"El reactivo {self.nombre} eliminado")
        else:
         print("No se elimino ningun reactivo")

    def esta_vencido(self):
        if datetime.now() > self.fecha_caducidad:
            print(f"El reactivo {self.fecha_caducidad} esta vencido")

    def dias_para_vencer(self):
        diferencia = self.fecha_caducidad - datetime.now()
        return diferencia.days

    def verificar_inventario_minimo(self):
            if self.inventario_disponible <= self.minimo_sugerido:
                print(f"¡Advertencia! El reactivo {self.nombre} está por debajo del mínimo.")

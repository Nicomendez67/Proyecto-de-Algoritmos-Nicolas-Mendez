
import random
import datetime
from Reactivos import GestionReactivos

class Recetas:
    def __init__(self, id, nombre, objetivo, reactivos_utilizados, procedimiento, valores_a_medir):
        
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados
        self.procedimiento = procedimiento
        self.valores_a_medir = valores_a_medir
        
  
    def show_attr(self):
        
        print("Informacion de recetas: ")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Objetivo: {self.objetivo}\n")
         
        print("Reactivos utilizados:")
        for i in self.reactivos_utilizados:
            for j, x in i.items():
                print(f"{j}: {x}")
                
        print("\n")      
        print("Procedimiento: ")
        for i in self.procedimiento:
            print(f"-> {i}")
        print("\n")
        
        print("Valores a medir: ")
        for i in self.valores_a_medir:
            for j, x in i.items():
                print(f"{j} - {x}")

class Experimento:
    def __init__(self, id, receta_id, responsables, fecha, costo_asociado, resultado):
        self.id = id
        self.receta_id = receta_id
        self.responsables = responsables
        self.fecha = fecha
        self.costo_asociado = costo_asociado
        self.resultado = resultado
        
    def show(self):
      
        resultado = "Los experimentos:\n"
        resultado += f"ID: {self.id}\n"
        resultado += f"Receta: {self.receta}\n"
        resultado += "Responsables:\n"
        for persona in self.responsables:
            resultado += f"{persona}\n"
        resultado += f"Fecha: {self.fecha}\n"
        resultado += f"Costo asociado: {self.costo_asociado}\n"
        resultado += f"Resultado: {self.resultado}\n\n"
        return resultado
       
    def crear_experimento(lista_experimentos):
        
        id = len(lista_experimentos)+1
        receta_id = int(input("ID de la receta: "))
        responsables = int(input("Número de responsables: "))
        p_responsables = []
        for i in range(responsables):
            personas = input("Nombre de los responsables: ")
            p_responsables.append(personas)
        fecha = input("Fecha de realizacion del experimento: ")
        costo_asociado = float(input("Costo: "))
        resultado = input("Resultado del experimento: ")

        nuevo_experimento = Experimento(id, receta_id, p_responsables, fecha, costo_asociado, resultado)
        lista_experimentos.append(nuevo_experimento)
        return nuevo_experimento, lista_experimentos
    
    
    def editar_experimento(self, nombre, atributo, nuevo_valor):

        nombre = input("Nombre del experimento a editar: ")
        atributo = input("Atributo del experimento a editar: ")
        nuevo_valor = input("Valor nuevo del atributo: ")
        for experimento in self.experimento:
            if experimento.nombre == nombre:
                if hasattr(experimento, atributo):
                    setattr(experimento, atributo, nuevo_valor)
                    print(f'Atributo "{atributo}" del experimento "{nombre}" actualizado a "{nuevo_valor}"')
                else:
                    print(f'El atributo "{atributo}" no existe en el experimento "{nombre}"')
                return
        print(f'No hay experimento con el nombre "{nombre}"')

        for experimento in self.experimento:
            if experimento.id == id:
                experimento.editar_atributo(atributo, nuevo_valor)
                return
            print(f'No se encontró un experimento con id: {id}')
                
    
    
    def eliminar_experimento(lista_experimentos, id_a_eliminar):
        del_id = int(input("ID del experimento a eliminar: "))
        for experimento in lista_experimentos:
            if experimento.id == del_id:
                lista_experimentos.remove(experimento)
                print(f"Experimento ({del_id}) eliminado correctamente.\n")
                return True
            else:
                print("ID no encontrado.\n")
                return False

    def realizar_experimento(self, receta, responsables, fecha):
        costo_total = 0
        for nombre, cantidad in receta.reactivos_necesarios.items():
            reactivo = next((r for r in self.gestion_reactivos.reactivos if r.nombre == nombre), None)
            if not reactivo or reactivo.inventario < cantidad or reactivo.esta_caducado():
                print(f"No se puede realizar el experimento. Reactivo {nombre} no disponible o caducado.")
                return
            costo_total += reactivo.costo * cantidad
            error_aleatorio = random.uniform(0.001, 0.225)
            cantidad_descontada = cantidad * (1 + error_aleatorio)
            reactivo.actualizar_inventario(-cantidad_descontada)
        experimento = Experimento(receta, responsables, fecha, costo_total)
        self.experimentos.append(experimento)
        self.gestion_reactivos.guardar_datos()
        self.guardar_datos()
        return experimento
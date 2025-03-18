import requests
from Gestion_reactivos import Gestion_reactivos
from Gestion_recetas import Gestion_recetas
from Gestion_Experimentos import Gestion_experimentos
from Reactivos import Reactivo
from Experimentos import Experimento
from datetime import datetime
import random 

class Laboratorio_quimico ():
    
    def obtener_json(self,url, params = None):
        try:
            response = requests.get(url, params = params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al acceder a la API: {e}")
            return None

    
    def start(self):
        self.reactivos_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json")
        self.recetas_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/recetas.json")
        self.experimentos_json=self.obtener_json("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json")

        lista_rc = Gestion_recetas.crear_recetas(self, self.recetas_json)
        lista_r =  Gestion_reactivos.crear_reactivos(self,self.reactivos_json)
        lista_e = Gestion_experimentos.crear_experimento(self, self.experimentos_json)
        
        while True:
    
            print("MENU DEL LABORATORIO QUIMICO")
    
    
            p1 = input("\n1------Ver Reactivos \n2------Ver Recetas \n3------Ver Experimentos \n4------Ver Estadisticas \n5------Salir")
            
            if p1 == "1":
                
                for i in self.reactivos:
                    i.show_attr()
                
                p1_reactivos = input("\n1------Crear Reactivo \n2------Editar Reactivo \n3------Eliminar Reactivo \n4------Ver fecha de Caducidad \n5------Regresar")
                
                if p1_reactivos == "1":
                    
                    Reactivo.crear_reactivos(lista_r)
                    print("Reactivo Creado")
                    
                if p1_reactivos == "2":
                
                    Reactivo.editar(lista_r)
                
                if p1_reactivos == "3":
                    
                    Reactivo.eliminar(self, lista_r)
                
                if p1_reactivos == "4":
                    
                    print("Fechas de caducidad de cada reactivo: \n")
                    for reactivo in self.reactivos:
                        if reactivo.esta_vencido():
                            print(f"- {reactivo.nombre} vencio el {reactivo.fecha_caducidad.date()}")
                        else:
                            print(f"- {reactivo.nombre} vence en {reactivo.dias_para_vencer()} días (Fecha: {reactivo.fecha_caducidad.date()})")
                if p1_reactivos == "5":
                    
                    pass
            elif p1 == "2":
                
                for i in self.recetas:
                    i.show_attr()
            
            elif p1 == "3":
                
                for i in self.experimentos:
                    i.show_attr()
                
                p1_experimentos = input("\n1------Crear Experimentos \n2------Editar Experimentos \n3------Eliminar Experimento \n4------Realizar Experimentos \n5------Regresar")
                
                if p1_experimentos == "1":
                    
                    lista_e = Experimento.crear_experimento(lista_e, lista_rc)
                    print("Reactivo Creado")
                    
                if p1_experimentos == "2":
                
                    Experimento.editar_experimento(self, None, None, None)
                
                if p1_experimentos == "3":
                    
                    Experimento.eliminar_experimento(lista_e, None)
                    lista_e.show()
                      
                if p1_experimentos == "4":
                    
                    cuenta = []
                    Experimento.realizar_experimento(self, cuenta)
                    
                if p1_experimentos =="5":
                    
                    pass
                    
            elif p1 == "4":
                pass
            
            elif p1 == "5": 
                
                print("Que tenga un buen dia!!!")
                pass 
            

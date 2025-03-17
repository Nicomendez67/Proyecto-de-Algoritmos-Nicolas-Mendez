from Reactivos import Reactivo, GestionReactivos
from Experimentos import Receta, GestionExperimentos
from Resultados import GestionResultados
from Estadisticas import Estadisticas
import datetime

def cargar_datos_api():
    # Aquí iría la lógica para cargar datos desde la API
    # Por ahora, vamos a simularlo con algunos datos de ejemplo
    reactivos_iniciales = [
        {"nombre": "Agua Destilada", "descripcion": "Agua purificada", "costo": 0.5, "categoria": "Disolvente", "inventario": 100, "unidad_medida": "L"},
        {"nombre": "Ácido Clorhídrico", "descripcion": "Solución al 37%", "costo": 2.0, "categoria": "Ácido", "inventario": 5, "unidad_medida": "L"},
        {"nombre": "Hidróxido de Sodio", "descripcion": "Perlas", "costo": 1.5, "categoria": "Base", "inventario": 10, "unidad_medida": "Kg"}
    ]
    gestion_reactivos = GestionReactivos()
    for reactivo_data in reactivos_iniciales:
        reactivo = Reactivo(**reactivo_data)
        gestion_reactivos.agregar_reactivo(reactivo)
    return gestion_reactivos

def main():
    # Cargar datos iniciales desde la API (simulado)
    gestion_reactivos = cargar_datos_api()

    # Inicializar gestores
    gestion_experimentos = GestionExperimentos(gestion_reactivos)
    gestion_resultados = GestionResultados(gestion_experimentos.experimentos)
    estadisticas = Estadisticas(gestion_experimentos, gestion_reactivos)

    # Ejemplo de uso
    # Crear una receta
    receta_ejemplo = Receta(
        nombre="Titulación Ácido-Base",
        objetivo="Determinar la concentración de un ácido",
        reactivos_necesarios={"Ácido Clorhídrico": 0.1, "Hidróxido de Sodio": 0.1},
        procedimiento="1. Preparar las soluciones... 2. Realizar la titulación..."
    )
    gestion_experimentos.crear_receta(receta_ejemplo)

    # Realizar un experimento
    experimento_realizado = gestion_experimentos.realizar_experimento(
        receta=receta_ejemplo,
        responsables=["Juan Pérez", "María García"],
        fecha=datetime.date.today().strftime('%Y-%m-%d')
    )

    if experimento_realizado:
        print("Experimento realizado con éxito.")

        # Simular resultados y verificar
        resultados_ejemplo = [7.0, 4.2]  # pH y volumen de titulación
        parametros_aceptables = [{"min": 6.8, "max": 7.2}, {"min": 4.0, "max": 4.5}]
        
        if gestion_resultados.verificar_resultados(experimento_realizado, resultados_ejemplo, parametros_aceptables):
            print("Resultados dentro de los parámetros.")
        else:
            print("Resultados fuera de los parámetros.")

    # Mostrar estadísticas
    print("\nEstadísticas:")
    print("Investigadores más activos:", estadisticas.investigadores_mas_activos())
    print("Experimentos más hechos:", estadisticas.experimentos_mas_menos_hechos())
    print("Reactivos de alta rotación:", estadisticas.reactivos_alta_rotacion())
    print("Reactivos más vencidos:", estadisticas.reactivos_mas_vencidos())

if __name__ == "__main__":
    main()
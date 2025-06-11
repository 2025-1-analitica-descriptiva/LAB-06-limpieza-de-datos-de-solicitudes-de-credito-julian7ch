"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
Escriba el código que ejecute la acción solicitada en la pregunta.
"""
import pandas as pd
import os

from homework.convertir_columna_sexo import convertir_columna_sexo
from homework.convertir_columna_tipo_de_emprendimiento import convertir_columna_tipo_de_emprendimiento
from homework.convertir_columna_idea_negocio import convertir_columna_idea_negocio
from homework.convertir_columna_barrio import convertir_columna_barrio
from homework.convertir_columna_monto_del_credito import convertir_columna_monto_del_credito
from homework.convertir_columna_fecha_de_beneficio import convertir_columna_fecha_de_beneficio
from homework.convertir_columna_linea_credito import convertir_columna_linea_credito
from homework.eliminar_datos_duplicados import eliminar_datos_duplicados

def pregunta_01():
    datos = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";").dropna()

    datos = convertir_columna_sexo(datos)
    datos = convertir_columna_tipo_de_emprendimiento(datos)
    datos = convertir_columna_idea_negocio(datos)
    datos = convertir_columna_barrio(datos)
    datos = convertir_columna_fecha_de_beneficio(datos)
    datos = convertir_columna_linea_credito(datos)
    datos = convertir_columna_monto_del_credito(datos)
    datos = eliminar_datos_duplicados(datos)

    # Crear carpeta output si no existe y guardar el archivo limpio
    os.makedirs(os.path.dirname("files/output/solicitudes_de_credito.csv"), exist_ok=True)
    datos.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.
    Realiza la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    Aplica transformación y depuración de datos según lo requerido,
    y guarda el archivo limpio en "files/output/solicitudes_de_credito.csv".
    """

if __name__ == "__main__":
    pregunta_01()
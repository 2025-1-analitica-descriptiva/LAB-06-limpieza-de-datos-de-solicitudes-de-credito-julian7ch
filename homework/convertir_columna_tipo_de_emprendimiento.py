def convertir_columna_tipo_de_emprendimiento(datos):
    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower()
    return datos

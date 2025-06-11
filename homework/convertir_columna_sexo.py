def   convertir_columna_sexo(datos):
    datos["sexo"] = datos["sexo"].str.lower()
    return datos

    
def convertir_columna_barrio(datos):
    datos["barrio"] = (
        datos["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )
    return datos
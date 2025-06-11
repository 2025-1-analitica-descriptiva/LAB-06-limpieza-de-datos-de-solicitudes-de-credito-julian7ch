def convertir_columna_idea_negocio(datos):
    datos["idea_negocio"] = (
        datos["idea_negocio"]
        # Conversion a minuscula
        .str.lower()
        #reemplazar _ por espacio
        .str.replace("_", " ", regex=False)
        #reemplazar - por espacio
        .str.replace("-", " ", regex=False)
        #quitar espacios en blanco
        .str.strip()
    )
    return datos
def convertir_columna_linea_credito(datos):
        # limpieza texto en 'línea_credito'
    datos["línea_credito"] = (
        datos["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    return datos
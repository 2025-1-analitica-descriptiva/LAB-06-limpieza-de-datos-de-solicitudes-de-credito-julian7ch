def convertir_columna_monto_del_credito(datos):
    # Realizar limpieza y parcear 'monto_del_credito' a float
    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
    return datos
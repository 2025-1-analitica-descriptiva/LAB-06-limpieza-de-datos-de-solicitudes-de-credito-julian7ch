def convertir_columna_fecha_de_beneficio(datos):
    # convertir fechas a formato DD/MM/YYYY   
    def ajustar_fecha(fecha):
        if fecha[0:4].isdigit():
            dia = fecha[8:10]
            mes = fecha[5:7]
            anio = fecha[0:4]
            return f"{dia}/{mes}/{anio}"
        else:
            return fecha


    # dar formato de fecha
    datos["fecha_de_beneficio"] = datos["fecha_de_beneficio"].apply(ajustar_fecha)
    return datos
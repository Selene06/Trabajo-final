def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw.get("sensor_id", "").strip()
    
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_limpia = ""
    for char in temp_raw:
        if char.isdigit() or char == '.' or char == '-':
            temp_limpia += char
            
    try:
        temperatura = float(temp_limpia)
    except ValueError:
        temperatura = 0.0
        
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion or ubicacion.strip() == "":
        ubicacion = "Planta Desconocida"
    else:
        ubicacion = ubicacion.strip()
        
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_limpios)
    
    if total_sensores == 0:
        return [], 0.0
        
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma_temperaturas += temp
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
            
    promedio_temperatura = suma_temperaturas / total_sensores
    return lista_sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31.2 C", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "19.0C", "ubicacion": "Planta Sur"}
    ]
    
    registros_limpios = [limpiar_registro_sensor(r) for r in registros_crudos]
    
    alertas, promedio = generar_resumen_sensores(registros_limpios, 25.0)
    
    print("REPORTE SENSORES")
    print("Registros limpios:", registros_limpios)
    print("Sensores en alerta (>25°C):", alertas)
    print(f"Promedio térmico global: {promedio:.2f}°C\n")

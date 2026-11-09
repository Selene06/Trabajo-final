import unittest
from django.shortcuts import render

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision

class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_nominal(self):
        self.assertEqual(calcular_emisiones_carbono(100), 40.0)
        
    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)
        
    def test_excepcion_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)

def obtener_metricas_consumo(registros):
    if not registros:
        return 0.0, None
        
    total_emisiones = 0.0
    mayor_consumo = -1
    planta_mayor = None
    
    for reg in registros:
        consumo = reg.get("consumo", 0)
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor = reg.get("planta")
            
    return total_emisiones, planta_mayor

def vista_panel_sustentabilidad(request):
    historial_plantas = [
        {"planta": "Planta norte", "consumo": 1500},
        {"planta": "Planta sur", "consumo": 3200},
        {"planta": "Planta este", "consumo": 900}
    ]
    
    total_emisiones, planta_mayor = obtener_metricas_consumo(historial_plantas)
    
    contexto = {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor,
        "registros": historial_plantas
    }
    
    return render(request, 'sustentabilidad/panel.html', contexto)

if __name__ == "__main__":
    unittest.main(exit=False)

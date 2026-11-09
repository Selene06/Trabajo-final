import json

class StockInvalidoError(Exception):
    pass

class DispositivoEcológico:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self._stock = 0
        self.stock = stock
            
    @property
    def stock(self):
        return self._stock
            
    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f"Error: El stock no puede ser negativo ({valor}).")
        self._stock = valor
        
    def ficha_tecnica(self):
        return f"Dispositivo: {self.nombre} | Stock: {self._stock}"

class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, stock, potencia_watts):
        super().__init__(nombre, stock)
        self.potencia_watts = potencia_watts
        
    def ficha_tecnica(self):
        return f"[Panel Solar] {self.nombre} | Potencia: {self.potencia_watts}W - Stock: {self.stock}"

class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        datos = []
        for disp in lista_dispositivos:
            datos.append({
                "nombre": disp.nombre,
                "stock": disp.stock,
                "ficha": disp.ficha_tecnica()
            })
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
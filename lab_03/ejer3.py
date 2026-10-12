class Sensor:
    tipo: str = "generico"
    def __init__(self, id_sensor: str, **kwargs):
        super().__init__(**kwargs)
        self.id = id_sensor
        self.encendido = False
    def activar(self):
        self.encendido = True
        print(f"censor [{self.id}] activado.")
    def desactivar(self):
        self.encendido = False
        print(f"censor [{self.id}] desactivado.")
class Camara(Sensor):
    tipo: str = "camara"
    def __init__(self, id_sensor: str, resolucion: str, **kwargs):
        self.resolucion = resolucion
        super().__init__(id_sensor=id_sensor, **kwargs)
class SensorLuzLaser(Sensor):
    tipo: str = "luz laser"
    def __init__(self, alcance: int, **kwargs):
        self.alcance = alcance
        super().__init__(**kwargs)
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo: str = "vehiculo autonomo"
    def __init__(self, id_sensor: str, resolucion: str, alcance: int):
        super().__init__(id_sensor=id_sensor, resolucion=resolucion, alcance=alcance)
    def mostrar_detalles(self):
        print(self.tipo)
        print(f"ID: {self.id} | Resolucion: {self.resolucion} | Alcance: {self.alcance} m | Activo: {self.encendido}")
if __name__ == "__main__":
    auto = VehiculoAutonomo("sen","5t",200)
    auto.activar()
    auto.mostrar_detalles()
    auto.desactivar()

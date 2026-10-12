import random
class Juego:
    def __init__(self, vidas: int):
        self.numeroDeVidas = vidas
        self._vidasActuales = vidas
        self.record = 0
    def reiniciaPartida(self):
        self._vidasActuales = self.numeroDeVidas
    def actualizaRecord(self):
        if self._vidasActuales > self.record:
            self.record = self._vidasActuales
            print(f"¡new records-vidas restantes:{self.record}!")
    def quitaVida(self)->bool:
        self._vidasActuales -= 1
        return self._vidasActuales > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print(f"\njuego adivina(0-10)---[Vidas:{self._vidasActuales}]")
        while self._vidasActuales > 0:
            try:
                ingresado=int(input("inserta el num: "))
            except ValueError:
                print("ingresa un número válido.")
                continue
            if ingresado == self.numeroAAdivinar:
                print("¡excelente!")
                self.actualizaRecord()
                return
            else:
                tiene_vidas = self.quitaVida()
                if tiene_vidas:
                    pista = "may" if ingresado < self.numeroAAdivinar else "menor"
                    print(f"intentalko de nuevo,el num es{pista},te quedan {self._vidasActuales} vidas")
                else:
                    print(f"perdiste,el num era: {self.numeroAAdivinar}")
                    return
if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()

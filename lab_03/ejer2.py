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
    def quitaVida(self) -> bool:
        self._vidasActuales -= 1
        return self._vidasActuales > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def validaNumero(self, numero: int) -> bool:
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print(f"\npartida(Vidas:{self._vidasActuales})")
        while self._vidasActuales > 0:
            try:
                ingresado = int(input("pon un num (0-10): "))
            except ValueError:
                continue
            if not self.validaNumero(ingresado):
                continue
            if ingresado == self.numeroAAdivinar:
                print("¡excelente!")
                self.actualizaRecord()
                return
            else:
                if not self.quitaVida():
                    print(f"game over,el num. era: {self.numeroAAdivinar}")
                    return
                print(f"incorecto,te falta {self._vidasActuales} vidas")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero: int) -> bool:
        if 0 <= numero <= 10:
            if numero % 2 == 0:
                return True
            print("error:el núm. debe ser par")
            return False
        print("error:fuera de rango (0-10).")
        return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero: int) -> bool:
        if 0 <= numero <= 10:
            if numero % 2 != 0:
                return True
            print("error:el número debe ser impar")
            return False
        print("error:fuera de rango (0-10)")
        return False
if __name__ == "__main__":
    print("probando los 3 Juegos")
    JuegoAdivinaNumero(3).juega()
    JuegoAdivinaPar(3).juega()
    JuegoAdivinaImpar(3).juega()

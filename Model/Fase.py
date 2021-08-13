class Fase:
    def __init__(self, numeroDaFase, textoDaFase):
        self.numeroDaFase = numeroDaFase
        self.textoDaFase = textoDaFase

    @property
    def numeroDaFase(self):
        return self._numeroDaFase

    @numeroDaFase.setter
    def numeroDaFase(self, numeroDaFase):
        self._numeroDaFase = numeroDaFase

    @property
    def textoDaFase(self):
        return self._textoDaFase

    @textoDaFase.setter
    def textoDaFase(self, textoDaFase):
        self._textoDaFase = textoDaFase
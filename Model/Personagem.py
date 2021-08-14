class Personagem:
    def __init__(self, name,
                 classe):  # construtor passa as características dos personagens na história, classes são apenas "personagem" e "inimigo"
        self._name = name
        self._classe = classe
        self._life = 0
        if self._classe == "personagem":
            self._life = 100
        else:
            self._life = 50

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def life(self):
        return self._life

    # @life.setter
    # def LifeSetter(self):
    #     if (self.classe == "personagem"):
    #         self._life = 100
    #     else:
    #         self._life = 50

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, classe):
        self._classe = classe

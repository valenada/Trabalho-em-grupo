class Tutorial:
    def __init__(self, name):
        self._name = name


    @property
    def GetName(self):
        return self._name


    def StartTutorial(self):
        print("Olá " + self.GetName + " seja bem vindo(a), caro herói. Espero que não tenha encontrado muitas dificuldades para seguir minhas instruções até aqui."
                                      "Esse é um mundo perigoso, onde cada escolha pode significar uma mudança irreversível em sua história."
                                      "Portanto, sempre pense bem antes de fazer suas escohas."
                                      "Para decidir o rumo de sua aventura, você deverá responder com 1, ou 2, conforme indicado"
                                      "ao lado de cada pergunta dividido por parênteses ()"
                                      "Você entendeu?")

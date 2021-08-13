class Tutorial:
    def __init__(self, name):
        self._name = name


    @property
    def GetName(self):
        return self._name


    def StartTutorial(self):
        print("Olá " + self.GetName + " seja bem vindo(a) a esta aventura, aqui bla bla bla bla não sei o que escrever auqi"
                                      "me ajuda carol............ este é um jogo de escolhas, para você jogar, você deverá"
                                      "escolher seus caminhos, para escolher, você deve responder com 1, ou 2, como estará indicado"
                                      "ao lado de cada pergunta dividido por parênteses ()") # carol revisa isso plssss

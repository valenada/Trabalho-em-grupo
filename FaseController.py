class FaseController:

    def tutorial(self):
        escolha = int(input(
            "Você entendeu? Posso repetir se quiser. Caso tenha entendido, escolha 1. Se quiser que eu repita, escolha 2."))

    if escolha == 1:
        self.escolhaUm()
    else:
        self.escolhaDois()

    def escolhaUm(self):
        print("Muito bem, você aprende rápido. Espero ter feito a escolha certa ao pedir sua ajuda.")

    def escolhaDois(self):
        print("Você é cauteloso, viajante. Isso é bom: sinal que você presta atenção."
                   "Em momentos difíceis, você irá se deparar com dois caminhos a seguir."
                   "Digite 1 ou 2 para fazer sua escolha, mas lembre-se que tudo tem consequências.")

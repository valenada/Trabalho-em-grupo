class FaseController:

    def tutorial(self):
        escolhaloop = int(input("Você entendeu? Posso repetir se quiser. Caso tenha entendido, escolha 1. Se quiser que eu repita, escolha 2."))

    if escolhaloop == 1:
        self.escolhaUm()
    else:
        self.escolhaDois()

    def escolhaUm(self):
        print("Muito bem, você aprende rápido. Espero ter feito a escolha certa ao pedir sua ajuda.")

    def escolhaDois(self):
        print("Você é cauteloso, viajante. Isso é bom: sinal que você presta atenção."
                   "Em momentos difíceis, você irá se deparar com dois caminhos a seguir."
                   "Digite 1 ou 2 para fazer sua escolha, mas lembre-se que tudo tem consequências.")

    def bebida(self):
        escolhabebida = int(input("Antes de eu te contar o que vai precisar fazer, imagino que esteja cansado, viajante."
                                  "Por favor, escolha uma bebida. Eu pago."
                                  "Se quiser Hidromel, escolha 1. Se quiser Sangue de Bruxa, digite 2."))
        if escolhabebida == 1:
            self.escolhaTres()
        else:
            self.escolhaQuatro()

    def escolhaTres(self):
        print("Você recebeu HIDROMEL. Tem um gosto bem normal.")
        print("Você é do tipo que não gosta de arriscar, não é?"
              "Sinto informar que vai arriscar muito nessa missão, mas o pagamento vai valer a pena, eu garanto.")

    def escolhaQuatro(self):
        print("Você recebeu uma garrafa de SANGUE DE BRUXA. É a melhor coisa que você já provou na vida!")
        print("Hmmm... Gostei de você. Você busca aventura nas menores coisas."
              "Agora tenho certeza de que você é a pessoa certa para esse serviço.")

    def missao(self):
        escolhamissao = int(input("Muito bem, chega de enrolação. Eu preciso de sua ajuda para encontrar o filho do meu patrão."
                                  "O menino é um pestinha e eu estava encarregado de cuidar dele, mas, durante a madrugada,"
                                  "o garoto sumiu, sem mais nem menos."
                                  "Não posso deixar meu patrão saber disso, ou ele vai cortar minha cabeça."
                                  "Acontece que... Eu não sou um lutador muito bom. Se eu for atrás do menino, seremos"
                                  "dois desaparecidos. Por favor, se você puder me ajudar, escolha 1. Se não... Escolha 2."))
        if escolhamissao == 1:
            print("Além de tudo você é uma pessoa bondosa! Obrigado," + self._Name + "sabia que podia contar com você.")

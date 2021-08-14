from Model import Personagem
import random


class Combat:
    def __init__(self, life1, life2):
        self._life1 = life1
        self._life2 = life2


    def atq(self):
        number = random.randint(0,1)
        if (number == 0):
            return 0
        else:
            return 1

    def dfs(self):
        number = random.randint(0, 1)
        if (number == 0):
            return 0
        else:
            return 1

    def twoAtqs(self):
        numberPersonagem = random.randint(0, 100)
        numberVilao = random.randint(0, 100)
        if numberPersonagem > numberVilao:
            return "personagem"


    def userChoice(self):
        choice = int(input("Você irá atacar ou defender neste turno? (1 para atacar e 0 para defender)"))
        botChoice = self.botChoice()
        atqPlayer = self.atq()
        atqBot = self.atq()
        dfsPlayer = self.dfs()
        dfsBot = self.dfs()
        if botChoice == 1:
            print("Seu adversário escolheu atacar")
        else:
            print("Seu adversário escolheu defender")
        if choice and botChoice == 1:   #se os dois atacam
            if self.twoAtqs() == "personagem":
                self._life2 -= 10
                print("Você atacou mais forte")
            else:
                self._life1 -= 10
                print("Ele atacou mais forte que você")
        if choice == 1 and botChoice == 0:   #se tu ataca e o bot defende
            if atqPlayer == 1 and dfsBot == 0:
                self._life2 -= 10
                print("Você acertou o ataque")
            if atqPlayer == 1 and dfsBot == 1:
                numberAtq = random.randint(0, 100)
                numberDfs = random.randint(0, 100)
                if numberAtq > numberDfs:
                    self._life2 -= 5
                    print("Você acertou o ataque, porém, mais fraco")
                else:
                    print("ataque defendido")
            if atqPlayer == 0:
                print("Você errou o ataque")
        if choice == 0 and botChoice == 0:   #os dois defendem
            print("Os dois defenderam")
        if choice == 0 and botChoice == 1:   #se tu defende e o bot ataca
            if atqBot == 1 and atqPlayer == 0:
                self._life1 -= 10
                print("Você não conseguiu defender")
            if atqBot == 1 and dfsPlayer == 1:
                numberAtq = random.randint(0, 100)
                numberDfs = random.randint(0, 100)
                if numberAtq > numberDfs:
                    self._life1 -= 5
                    print("Ele conseguiu atacar você, porém, mais fraco")
                else:
                    print("ataque defendido")
            if atqBot == 0:
                print("Ele errou o ataque")
        print("você ficou com " + str(self._life1) + " de vida e seu adversário ficou com " + str(self._life2))










    def botChoice(self):
        choice = random.randint(0, 1)
        if choice == 1:
            return 1
        else:
            return 0

    def combat(self):
        while (self._life1 and self._life2 > 0):
            self.userChoice()
        if self._life1 > 0:
            print("Você ganhou a batalha e ficou com " + str(self._life1) + " de vida")
        else:
            print("Você perdeu, game over")

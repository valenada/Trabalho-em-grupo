from Model import Personagem
from View import TelaDeLogin
import TutorialController
import CombatController


class MainController:
    telaLogin = TelaDeLogin.TelaDeLogin(str(input("Qual o nome do seu personagem? ")))
    personagem = Personagem.Personagem(telaLogin.GetName(), "personagem")


    def escolha(Login):
        escolha = str(input("O nome do seu personagem é: " + Login.name + ", deseja alterar?").lower())
        if (escolha == "sim"):
            Login.name = str(input("Ok, escolha seu novo nome: "))
        print("O nome escolhido para o seu personagém é: " + Login.name)

    escolha(personagem)

    tutorial = TutorialController.Tutorial(personagem.name)
    tutorial.StartTutorial()

    vilao = Personagem.Personagem("vilão 1", "vilão")

    CombatController.Combat(personagem.life, vilao.life).combat()



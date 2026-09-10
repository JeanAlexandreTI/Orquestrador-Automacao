import os 
# TESTEEEE

class Organiza_Auto():
    def __init__(self):
        self.__list_automacoes = []
        self.__nome = None
        self.__intervalo = None
        self.__objetivo = None
        self.__ativo = None
        self.__caminho = None

    def voltar_menu(self, texto = "\n"):
        print(texto)
        input("\nInforme qualquer tecla para retornar ao menu: ")
        self.opcao_menu()


    def menu(self):
        print("""Escolha entre as alternativas:
        [ 1 ] - CADASTRAR AUTO
        [ 2 ] - ATIVAR/DESATIVAR AUTO
        [ 3 ] - LISTAR AUTO
        [ 4 ] - SAIR
    """)


    def verifica_caminho(self, caminho):

        if os.path.exists(caminho):
            print("\nCaminho da estrutuda automatizada existente.")

            dict_dados ={
                "nome": self.__nome,
                "intervalo": self.__intervalo,
                "objetivo": self.__objetivo,
                "ativo": self.__ativo,
                "caminho": self.__caminho,
                    }

            self.__list_automacoes.append(dict_dados)
            self.voltar_menu(f"{self.__nome} foi devidamente cadastrado.")

        else:
            self.voltar_menu("\nRegistre um caminho existente.")


    def cadastrar_auto(self):
        self.__nome= input("Nome da estrutura automatizada: ").upper().strip()
        self.__intervalo= int(input("Intervalo de execucao da estrutura (segundos): "))
        self.__objetivo= input("Resumo referente a estrutura: ").upper().strip()
        self.__ativo= False
        self.__caminho= input("Caminho da estrutura que deve rodar: ").strip()

        self.verifica_caminho(self.__caminho)


    def ativar_auto(self):
        pesquisa_auto = input("Nome da estrutura procurada: ").upper().strip()
        for i in self.__list_automacoes:
            if i[self.__nome] == pesquisa_auto:
                print(f"{i[self.__nome]} passou de {'ATIVO' if i[self.__ativo] else 'DESATIVO'} para:", end=" ")
                i[self.__ativo] = not i[self.__ativo]
                print(f"{'ATIVO' if i[self.__ativo] else 'DESATIVO'}")


    def listar_auto(self):
        pesquisa_auto = input("Nome da estrutura procurada: ").upper().strip()
        pesquisa_encontrada = False

        print(self.__list_automacoes)

        for i in self.__list_automacoes:
            if i[self.__nome] == pesquisa_auto:
                pesquisa_encontrada = True
                print(i)

        if pesquisa_encontrada:
            self.voltar_menu()
        else:
            self.voltar_menu("\nEstrutura inexistente.")


    def opcao_sair(self):
        os.system("clear" if os.name != "nt" else "cls")
        print("Sistema encerrado.")


    def valor_incorreto(self):
        self.voltar_menu("\nERROR! Informe um valor numerico.")


    def opcao_menu(self):
        self.menu()

        try:
            opcao_escolhida = int(input("Escolhido: "))

            if opcao_escolhida == 1:
                self.cadastrar_auto()

            elif opcao_escolhida == 2:
                self.ativar_auto()

            elif opcao_escolhida == 3:
                self.listar_auto()

            elif opcao_escolhida == 4:
                self.opcao_sair()

            else:
                self.voltar_menu("\nValor informando ausente.")

        except ValueError:
            self.valor_incorreto()



class Automacao():
    def __init__(self):
        pass


def main():
    Organiza_Auto().opcao_menu()


if __name__ == "__main__":
    main()
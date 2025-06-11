from controller.controle_produtos import ControleEstoque

class Interface:
    def __init__(self):
        self.controle = ControleEstoque()

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Inserir produtos")
            print("2. Deletar produtos")
            print('3. Atualizar o preço')
            print('4. Consultar produto')
            print('5. Valor total do estoque')
            print('6. Listar produtos')
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir()
            elif opcao == '2':
                self.deletar()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.consulta()
            elif opcao == '5':
                self.total()
            elif opcao == "6":
                self.listar()
            elif opcao == "7":
                print("Encerrando...")
                print('Finalizado')
                break
            else:
                print("Opção inválida.")

    def inserir(self):
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        mensagem = self.controle.inserir(nome,quantidade,preco)
        print(mensagem)

    def deletar(self):
        id = input('informe o produto que deseja excluir pelo id:')
        mensagem = self.controle.delt(id)
        print(mensagem)

    def atualizar(self):
         inf = int(input('Digite o id do produto que deseja alterar: '))
         nova_qtd = int(input('Nova quantidade: '))
         mensagem = self.controle.atualizar(nova_qtd,inf)
         print(mensagem)


    def total(self):
        produto = self.controle.tati()
        print('\n--- A quantidade total de \nprodutos no estoque é:',produto, '''---''')

    def listar(self):
        produtos = self.controle.listar()
        print("\n--- Produtos Cadastrados ---")
        for f in produtos:
            print(f"ID: {f[0]} | Nome: {f[1]} | Quantidade: {f[2]} | Preço: R${f[3]:.2f}")

    def consulta(self):
        x = input('\n---Informe por onde dejesa buscar \nNome(N) ou ID(I)---')
        if x == 'N':
            nome = input('Indorme o nome: ')
            busca = self.controle.busque(nome)
            print(busca)
            
        elif x == 'I':
                id = int(input('Informe o id: '))
                busca = self.controle.busque(id)
                print(busca)

        else:
            print('Opção Invalida!')

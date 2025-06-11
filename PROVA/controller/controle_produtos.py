from model.produto import Produto
from model.produto_dao import ProdutoDAO

class ControleEstoque():
    def __init__(self):
        self.dao = ProdutoDAO()

    def inserir(self, nome, quantidade, preco):
        produto = Produto(nome, quantidade, preco)
        self.dao.inserir(produto)
        
        if preco <= 0:
            print('Não é possível continuar...')
        elif quantidade <= 0:
            print('Não é possível continuar...')

        else:
            return "Produto inserido com sucesso!"


    
    def delt(self,id):
        apagar = id
        self.dao.delet(apagar)
        return '\n--- Produto deletado com sucesso! ---'
    
    def upar(self):
        return self.dao.updat()

    def tati(self):
        return self.dao.toti()

    def listar(self):
        return self.dao.listar_todos()
    
    def busque(self, id, nome):
        con = (id,nome)
        self.dao.busc(con)
        return "Produto encontrado"
        

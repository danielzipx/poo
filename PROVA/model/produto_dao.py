import sqlite3

class ProdutoDAO:
    def __init__(self):
        self.conn = sqlite3.connect('database/produtos.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
        )
        ''')
        self.conn.commit()

    def inserir(self, produto):
        self.cursor.execute('''
            INSERT INTO produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
        ''', (produto.nome, produto.quantidade, produto.preco))
        self.conn.commit()

    def delet(self):
        self.cursor.execute('DELETE FROM produtos WHERE id = ?')
    
    def updat(self):
        self.cursor.execute('SELECT * FROM produtos WHERE id = ?')  

        self.cursor.execute('''
                            UPDATE produtos
                            SET quantidade = ?
                            WHERE id = ?
                            ''')
    
    def toti(self):
        self.cursor.execute('SELECT SUM(quantidade) FROM produtos')
        return self.cursor.fetchone()[0]
    
    def busc(self,con):
        self.cursor.execute('SELECT nome, id FROM produtos WHERE nome, id = ?, ?', (con.nome, con.id))
        

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='jogo',
)
cursor = conexao.cursor()

# CRUD
'''# CREATE
nome_produto1 = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# UPDATE
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados'''

# READ (UPDATE)
comando = f'SELECT * FROM loja'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

comando = f'SELECT * FROM botao'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

cursor.close()
conexao.close()

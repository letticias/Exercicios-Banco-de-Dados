import sqlite3

conexao = sqlite3.connect('bancos')
cursor = conexao.cursor()

#5. Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: id (chave primária), 
#nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT, PRIMARY KEY (id));')

cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Ive", 28, 1350.0)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Andrea", 27, 315.7)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"João", 31, 600.0)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Patricia", 29, 1250.5)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Lara", 33, 123.5)')

#6. Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for cliente in dados:
    print(cliente)

#b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes;')

# Imprima o saldo médio
print("O saldo médio dos clientes é:", cursor.fetchone()[0])

#c) Encontre o cliente com o saldo máximo.
#buscando saldo maximo
cursor.execute('SELECT MAX(saldo) FROM clientes')
saldo_max = cursor.fetchone()[0]
print(saldo_max)

#cliente com saldo maximo
cursor.execute('SELECT nome FROM clientes WHERE saldo = 1350.0;')
cliente_saldo_max = cursor.fetchone()[0]
print("O cliente com maior saldo se chama", cliente_saldo_max)

#d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT * FROM clientes WHERE saldo >1000')
n=1
for cliente in dados:
    print(n)
    n=n+1
print( n-1, 'clientes têm saldo acima de 1000')

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 600 WHERE nome="Lara"')

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes where id=2')

#8. Junção de Tabelas: Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real).
cursor.execute('CREATE TABLE compras (id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT, PRIMARY KEY (id), FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1,"camiseta",29.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2,3,"camiseta",35.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3,4,"bolsa",140.00)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4,5,"sapato",79.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(5,1,"carteira",49.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(6,4,"chinelo",32.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(7,1,"saia",39.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(8,3,"camiseta",28.90)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(9,4,"bolsa",135.50)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(10,5,"sapato",82.00)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute('SELECT c.nome AS nome_cliente, co.produto, co.valor FROM clientes c INNER JOIN compras co ON c.id = co.cliente_id;')
for cliente in dados:
    print(cliente)

conexao.commit()

conexao.close

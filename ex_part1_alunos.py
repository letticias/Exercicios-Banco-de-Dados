import sqlite3

conexao = sqlite3.connect('bancos')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Isa", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Ana", 17, "Biologia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Jonas", 21, "Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Patrick", 19, "Eletrotecnico")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Lara", 18, "Fisica")')

#3. Consultas Básicas -  Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
for aluno in dados:
    print(aluno)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
for aluno in dados:
    print(aluno)

#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT * FROM alunos')
n=1
for aluno in dados:
    print(n)
    n=n+1

print('A tabela possui ', n-1, 'alunos')

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=18 WHERE nome="Ana"')

#dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id=4')

dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)


conexao.commit()

conexao.close

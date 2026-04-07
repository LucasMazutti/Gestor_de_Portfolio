filmes = []

while True:
    primeiro_comando = str(input("Digite 'about' para saber mais ou 'quit' para sair: ")).lower()
    if primeiro_comando == "about":
        print("Gestor de filmes do Lucas Mazutti!")
        primeiro_comando = str(input("Digite add para adicionar filmes: ")).lower()
    if primeiro_comando.startswith("add"):
        numero_filmes = int(input("Numero de filmes que queira adicionar -> "))
        if numero_filmes <= 0:
            print("Valor incorreto, digite um número maior que zero.")
        else:
            for i in range(numero_filmes):
                nome_filme = input(f"Digite o nome do filme {i+1}: ")
                filmes.append(nome_filme)
                print(f"SUCESSO: Filme '{nome_filme}' adicionado.")
            print("Filmes adicionados!")
    elif primeiro_comando == "list":
        if len(filmes) == 0:
            print("Nenhum filme cadastrado.")
        else:
            contador = 1
            for filme in filmes:
                print(f"{contador}. {filme}")
                contador += 1
    elif primeiro_comando == "quit":
        print("Você saiu do gestor de filmes, até logo!")
        break
    else:
        print("Valor não reconhecido, digite 'about', 'add', 'list' ou 'quit'.")


'''
inicio - "about"
fim - "projetos adicionados"

1. usuario digita about e segue para uma mensagem de boas vindas
 - após isso uma segunda mensagem pedindo add
 - se digitar quit, mensagem de despedida.
 - outra coisa, erro e voltar ao inicio
2. ao digitar add vai para o numero de projetos que o usuario quer adicionar
 - se digitar outra coisa apenas refaz a mesma situação.
3. ao digitar o numero de projetos para adicioonar(não pode ser 0 nem menor que 0) 4 eetapa.
 - se menor igual a zero, mensagem de erro e retrornando ao menu principal do para ele 
 digitar o numero corretamente.
4. Digitandoo o numeoro de projetos, o sistema pede para escrever o nome dos projetos.
5. após isso, mensagem de sucesso, projets gravados.

codigo atual->
while True:
    primeiro_comando = str(input("Digite 'about' para saber mais ou 'quit' para sair: ")).lower()
    if primeiro_comando == "about":
        print("Gestor de projetos do Lucas Mazutti!")
        primeiro_comando = str(input("Digite add para adicionar o número de projetos: ")).lower()
    if primeiro_comando.startswith("add"):
        numero_projetos = int(input("Numero de projetos que queira adicionar -> "))
        if numero_projetos <= 0:
            print("Valor incorreto, digite um número maior que zero.")
        else:
            for i in range(numero_projetos):
                nome_projeto = input(f"Digite o nome do projeto {i+1}: ")
                print(f"SUCESSO: Projeto '{nome_projeto}' adicionado.")
            print("Projetos adicionados!")
    elif primeiro_comando == "quit":
        print("Você saiu do gestor de projetos, até logo!")
        break
    else:
        print("Valor não reconhecido, digite 'about', 'add' ou 'quit'.")
'''



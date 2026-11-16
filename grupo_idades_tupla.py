pessoas = []


print("=== Cadastro de 10 Pessoas ===")
for i in range(10):
    print(f"\nPessoa {i + 1}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    
    pessoa_tupla = (nome, idade)
    pessoas.append(pessoa_tupla)


print("\n=== Grupo 1: Pessoas com menos de 18 anos ===")
for pessoa in pessoas:
    # pessoa[0] é o nome e pessoa[1] é a idade dentro da tupla
    if pessoa[1] < 18:
        print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]} anos")


print("\n=== Grupo 2: Pessoas com 18 anos ou mais ===")
for pessoa in pessoas:
    if pessoa[1] >= 18:
        print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]} anos")

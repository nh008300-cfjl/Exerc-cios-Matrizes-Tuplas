
matriz = [[0 for _ in range(3)] for _ in range(3)]


print("=== Digite os valores da Matriz 3x3 ===")
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Elemento [{i+1}][{j+1}]: "))


eh_identidade = True

for i in range(3):
    for j in range(3):
        
        if i == j and matriz[i][j] != 1:
            eh_identidade = False
        
        elif i != j and matriz[i][j] != 0:
            eh_identidade = False

print("\n=== Matriz Informada ===")
for linha in matriz:
    print(linha)

if eh_identidade:
    print("\nResultado: A matriz informada É uma matriz identidade!")
else:
    print("\nResultado: A matriz informada NÃO é uma matriz identidade.")

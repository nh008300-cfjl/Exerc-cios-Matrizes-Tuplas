
matriz_a = [[0 for _ in range(3)] for _ in range(4)]
matriz_b = [[0 for _ in range(3)] for _ in range(4)]
matriz_soma = [[0 for _ in range(3)] for _ in range(4)]


print("=== Digite os valores da Matriz A (4x3) ===")
for i in range(4):
    for j in range(3):
        matriz_a[i][j] = float(input(f"Matriz A [{i+1}][{j+1}]: "))

print("\n=== Digite os valores da Matriz B (4x3) ===")
for i in range(4):
    for j in range(3):
        matriz_b[i][j] = float(input(f"Matriz B [{i+1}][{j+1}]: "))


for i in range(4):
    for j in range(3):
        matriz_soma[i][j] = matriz_a[i][j] + matriz_b[i][j]


print("\n=== Matriz Resultante (Soma) ===")
for i in range(4):
    for j in range(3):
        
        print(f"{matriz_soma[i][j]:8.2f}", end=" ")
    print() 

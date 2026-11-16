# Criando a matriz 3x3 vazia
M = [[0 for _ in range(3)] for _ in range(3)]

# Entrada de dados dos 9 elementos
print("=== Digite os valores da Matriz 3x3 ===")
for i in range(3):
    for j in range(3):
        M[i][j] = float(input(f"Elemento [{i+1}][{j+1}]: "))

# Associando cada posição da matriz às letras da fórmula
a, b, c = M[0][0], M[0][1], M[0][2]
d, e, f = M[1][0], M[1][1], M[1][2]
g, h, i = M[2][0], M[2][1], M[2][2]

# Calculando o determinante pela Regra de Sarrus
detM = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)

# Exibindo a matriz e o resultado
print("\n=== Matriz Informada ===")
for linha in M:
    print(linha)

print(f"\nO determinante da matriz 3x3 é: {detM}")

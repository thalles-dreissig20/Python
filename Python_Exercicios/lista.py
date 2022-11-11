
numeros = []
valores = []
repetidos = set()
N = int(input("Quantidade: "))

for i in range(N):
    numeros.append(int(input("Número: ")))
    
for numero in numeros:
    if numero not in valores:
        valores.append(numero)
    else:
        repetidos.add(numero)

print(f"Valores = {numeros}")
print(f"Repetidos = {repetidos}")

N = int(input("Lista: "))
multiploDois = 0
multipleTres = 0
multipleQuatro = 0
multipleCinco = 0

values = input().split(' ')
valores = values[:N]
for i in range(N):
    valores[i] = int(valores[i])
    if(valores[i] % 2 ==0):
        multiploDois+=1
    if(valores[i] % 3 ==0):
        multipleTres+=1
    if(valores[i] % 4 ==0):
        multipleQuatro+=1
    if(valores[i] % 5 ==0):
        multipleCinco+=1
print('{0} Multiplo(s) de 2'.format(multiploDois))
print('{0} Multiplo(s) de 3'.format(multipleTres))     
print('{0} Multiplo(s) de 4'.format(multipleQuatro))     
print('{0} Multiplo(s) de 5'.format(multipleCinco)) 
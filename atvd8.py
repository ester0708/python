n1 = int(input("digite um numero"))
n2 = int(input("digite um numero"))
n3 = int(input("digite um numero"))
maior = n1 
menor = n1 
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
meio = (n1 + n2 + n3) - maior - menor
print ("os numeros em ordem decrescente são:", maior, meio, menor)
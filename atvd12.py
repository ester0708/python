na = int(input("digite o número de identificação do aluno"))
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
ME = float(input("digite a média dos exercícios: "))
MA = (n1 + n2 *2 + n3 *3 + ME)/7
if MA >= 90:
    print("A, aporvado")
elif MA >= 75:
    print("B, aprovado")
elif MA >= 60:
    print("C, aporvado")
elif MA >= 40:
    print("D, reprovado")
else:
    print("E, reprovado")
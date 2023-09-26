a = float(input("digite sua altura"))
p = float(input("digite seu peso"))
resultado = p / (a*a)
print(round(resultado, 1))
if resultado < 18.5:
    print("Abaixo do peso")
if resultado > 18.5 and resultado < 25:
    print("Peso normal")
if resultado > 25 and resultado < 30:
    print("Acima do peso")
if resultado > 30:
    print("Obeso")
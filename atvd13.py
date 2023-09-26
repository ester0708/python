s = float(input("Digite seu salário"))
if s <= 2112.00:
    print("Você está isento de pagar o imposto de renda")
elif s <= 2826.65:
    print(s-158.40)
elif s <= 3751.05:
    print(s-370.40)
elif s <= 4664.68:
    print(s-651.73)
else:
    print(s-884.96)
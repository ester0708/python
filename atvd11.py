p = float(input("digite o preço"))
print("Forma de pagamento 1, à vista com dinheiro ou cheque")
print("Forma de pagamento 2, à vista com cartão de crédito")
print("Forma de pagaemento 3, em duas vezes")
print("Forma de pagamento 4, duas vezes com juros")
fp = input("digite a forma de pagamento")
if fp == "1":
    print (p - (p*0.10))
elif fp == "2":
    print(p-(p*0.15))
elif fp == "3":
    print(p/2)
elif fp == "4":
    pcj = p*0.10
    print(p-pcj)
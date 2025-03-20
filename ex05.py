maca = int(input("qtd de maças:"))


if(maca >= 12):
    preco = 1.00
else:
    preco = 1.30

total = maca * preco
print("O total é de:",total, "Reais")

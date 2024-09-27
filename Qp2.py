import os 
os.system("cls")

idade = int(input("Digite a idade do atleta: "))

if idade >= 16 and idade <= 18 :
    print("O atrela joga no juvenil.")
elif idade >= 14 and idade <= 15 :
    print("O atleta joga no infantil.")
elif idade >= 13 and idade <= 12 :
    print("O atleta joga no mirim.")
elif idade >= 10 and idade <= 11 :
    print("O atlata joga no Pre-Mirim.")
else :
    print("Categoria não registrada.")

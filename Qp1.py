import os 
os.system("cls")

total_carros = 0
carro_mais_rapido = 0
carro_mais_novo =  0

while True :
    marca = input("Digite a marca do carro: ")
   
    if marca == 'n' or marca == 'N' :
        break
    
    ano = int(input("Digite o ano do carro: "))

    vel = int(input("Informe a velocidade final do carro: "))


    total_carros += 1

    if vel > carro_mais_rapido :
        carro_mais_rapido = vel

    if ano > carro_mais_novo :
        carro_mais_novo = ano


print("Quantidade de carros cadasttrados : ",total_carros)
print("Carro mais novo é do ano ",ano)
print("e o carro mais rápido tem a valocidade igual a: ",vel,"K/H")

    
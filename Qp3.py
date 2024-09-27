import os 
os.system("cls")

direita = 0
esquerda = 0
incorreta = 0 
i = 0

while i < 10 :
    resposta = input("Você está indo para a direita ou esquerda? ")

    i += 1

    if resposta == "Direita" or resposta == "Dir" or resposta == "D" :
        direita += 1

    elif resposta == "Esquerda" or resposta == "Esq" or resposta == "E" :
        esquerda += 1
    
    elif resposta != "Direita" or resposta != "Dir" or resposta != "D" or resposta != "Esquerda" or resposta != "Esq" or resposta != "E" :
        incorreta += 1

print("Curvas a direita : ",direita)
print("Curvas a esquerda : ",esquerda)
print("incorretas : ",incorreta)
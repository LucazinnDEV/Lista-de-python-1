import os 
os.system("cls")

quantidade = int(input("Digite a quantidade de alunos: "))

total_m = 0
total_f = 0
masc = 0
fem = 0
i = 0

while i < quantidade :
   
    genero = input("Informe o gênero do estudante (M/F): ")
    
    altura = float(input("Informe a altura do estudante (em metros): "))

    if genero == "M" or genero == "m" :
        total_m += altura
        masc += 1
    elif genero == "F" or genero =="f" :
        total_f += altura
        fem += 1
    else :
        print("Gênero inválido. Por favor, digite M para masculino ou F para feminino.")

    i += 1

    if masc > 0 :
        media_m = total_m / masc
    else :
        media_m = 0

    if fem > 0 :
        media_f = total_f / fem
    else :
        media_f = 0

print("total de alunos :",quantidade)
print("A média dos alunos foi de :",media_m,"Metros")
print("A média das alunas foi de :",media_f,"Metros")


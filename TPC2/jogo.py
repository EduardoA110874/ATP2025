
n = 21  

print("Jogo dos Fósforos")
print("Há", n, "fósforos. Perde quem tirar o último!")

primeiro = input("Quem começa? (jogador/computador): ")
while primeiro!="jogador" and primeiro!="computador":
    primeiro=input("Opcção inválida! Quem começa? (jogador/computador): ")
vez = primeiro  

while n > 0:
    print(f"Restam {n} fósforos.")

    if vez == "jogador":
        jogada = int(input("Quantos fósforos quer tirar (1-4)? "))

        while jogada < 1 or jogada > 4 or jogada > n:
            jogada = int(input("Jogada inválida! Quantos fósforos quer tirar? (1-4): "))

    else:
        print("Vez do computador")

        if 4<n<=20:
            jogada = 5 - jogada
            if jogada == 0:
                jogada = 1
        else:
            if 1<n<=4:
                jogada = n - 1
            else:
                jogada = 1 

        print(f"O computador tirou {jogada} fósforos.")

    n = n-jogada

    if n == 0:
        print(f"{vez} tirou o último fósforo... {vez} PERDEU!")
        break

    if vez == "jogador":
        vez = "computador"
    else:
        vez = "jogador"

#Faça um programa que permita ao usuário  digitar a quantidade de vitorias, empates e derrotas de um time de futebol e
# Ao final informe o numero de jogos que esse time  disputou. E o numero de pontos obtidos (Vitoria 3, Empate 1)

valorV = int(input("Quantidade de Vitorias: "))
valorE = int(input("Quantidade de Empates: "))
valorD = int(input("Quantidade de Derrotas: "))
valorT = valorV+valorE+valorD
valorPontos = valorV*3+valorE*1
print ("Numero total de partidas jogadas pela PNG: ", valorT, "Com um total de: ", valorPontos, "pontos")


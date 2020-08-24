#Um programa que permita o usuário digitar o valor unitario e a quantidade de um produto
# no final um valor a pagar

valorUnitario = float(input("Digite o valor R$:"))
quantidadeProduto = float(input("Digite a quantidade:"))
valorTotal = valorUnitario*quantidadeProduto
print ("O valor total do produto é :R$ ", round (valorTotal), "Reais")
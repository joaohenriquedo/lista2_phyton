#escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "cada cliente deve pagar:"x valor
conta = int (input("qual o valor total da conta?"))
cliente = int (input("quantos clientes existem?"))
final = conta / cliente
print("cada cliente deve pagar", final)

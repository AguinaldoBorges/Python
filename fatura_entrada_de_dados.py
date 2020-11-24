#Entrada de dados e devolve o status da fatura
#desenvolvido por: Aguinaldo Borges

print("============================================")
print("             CONSULTA/FATURA") #título da aplicação
print("============================================\n")

#entrada de dados digitados pelo usuário
nome = input("Digite o nome do cliente: ")
vencimento = input("Digite o dia de vencimento:")
mes = input("Digite o mês de vencimento:")
valor = input("Digite o valor da fatura: ")

#saída de dados (informa o status da fatura)
print("\n============================================")
print("Olá ",nome)
print("A sua fatura com vencimento em ",vencimento," de ",mes," \nno valor de R$ ",valor," está fechada")
print("============================================")

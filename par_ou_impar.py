#condicionais - Par ou Impar
#desenvolvido por: Aguinaldo Borges

print("============================================")
print("             PAR OU IMPAR") #título da aplicação
print("============================================\n")

#entrada de dados: número inteiro 
numero = int(input("Digite um número inteiro: "))
res = numero%2
#saída de dados: (informa sé o número é par ou ímpar)
print("\n============================================")
if res==0:
    print("O número ",numero," é PAR!")
else:
    print("O número ",numero," é IMPAR!")
print("============================================")

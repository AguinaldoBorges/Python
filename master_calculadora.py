#Programa:
#Desenvolvedor: Aguinaldo Borges

print("=====================")
print(" MASTER CALCULADORA")#Titulo
print("=====================")

operacao=9#Declaracao da variavel

try:
	while operacao!=0:
		#Usuario escolhe a operacao que vai usar
		operacao=int(input("\n*** ***\nEscolha a operação:\nPara SOMA digite 1\nPara SUBTRAÇÃO digite 2\nPara DIVISÃO digite 3\nPara MULTIPLICAÇÃO digite 4\nPara SAIR digite 0\n:"))


#OPERACOES===================== 	
		if operacao==1:#SOMA
			num= int(input("Digite um numero inteiro: "))
			mult=int(input("Digite outro numero inteiro: "))
			res=num+mult
			print("\n",num," + ",mult," = ",res)			
		if operacao==2:#SUBTRACAO
			num= int(input("Digite um numero inteiro: "))
			mult=int(input("Digite outro numero inteiro: "))
			res=num-mult
			print("\n",num," - ",mult," = ",res)			
		if operacao==3:#DIVISAO
			num= int(input("Digite um numero inteiro: "))
			mult=int(input("Digite o divisor (numero inteiro): "))
			res=num/mult
			print("\n",num," / ",mult," = ",res)
				
		if operacao==4:#MULTIPLICACAO
			num= int(input("Digite um numero inteiro: "))
			mult=int(input("Digite o multiplicador (numero inteiro): "))
			res=num*mult
			print("\n",num," x ",mult," = ",res)
		if operacao>4:
			print("Operação inválida")
		if operacao<0:
			print("Operação inválida")	
			
except:#TRATAMENTO DE ERRO - Caso o usuario digite uma letra ou caracterr especial
	print("Ops! A Master Calculadora só aceita números.\nAfinal, não dá para calcular letras ou caracteres não é?")

#Mensagem de encerramento do programa
print("\nObrigado por usar a MASTER CALCULADORA!")
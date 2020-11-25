#Programa: Magic CEP
#desenvolvido por: Aguinaldo Borges

#importa biblioteca
import pycep_correios

print("============================================")
print("     MAGIC CEP - Encontre um endereço aqui") #título da aplicação
print("============================================\n")

chave = True #Cindição que Inicia o loop

#loop
while chave==True:
    try: #Tratamento de erro
        cep = input("Digite o CEP sem pontos e traços: ") #Entrada de dados do usuário
        end = pycep_correios.get_address_from_cep(cep) #processando na biblioteca
        print(end) #Exibindo resultado

        #Pergunta ao usuário se deseja sair ou continuar fazendo uma nova consulta
        continuar = input("\nDeseja fazer nova consulta?\nSIM - Digite 1:\nNÃO - Digite 2:\nSIM/NÃO: ")
        if continuar == "1":
            print("\nNOVA CONSULTA:\n")
        else:
            chave=False #encerra o Loop
            
    except: #Mensagem de erro
        print("\nOOOPS! Algo deu errado. Verifique o CEP desejado e digite novamente. \nLembre-se de digitar somente os números\n")
    
print("\n============================================")
print("Obrigado por usar o !") #Mensagem de encerramento
print("============================================")

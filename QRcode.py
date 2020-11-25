#Programa: Gerador de qrCode
#Desenvolvedor: Aguinaldo Borges

#Importa biblioteca
import pyqrcode
print("====================")
print(" QR CODE GENERATOR")
print("====================\n")
#Entrada de dados digitados pelo usuario
text = input("Digite o conteúdo a ser convertido para QR Code: ")
nome = input("Digite o nome do arquivo: ")
nomearquivo=nome+".html"

#processamento: criacção do QR code
try:
	url=pyqrcode.create(text)
	url.svg(nomearquivo,scale=10)
	print("QR code criado com sucesso!")
except:
	#tratamento de erro: mensagem exibida em caso de erro.
	print("Ops! Algo de errado não está certo!")

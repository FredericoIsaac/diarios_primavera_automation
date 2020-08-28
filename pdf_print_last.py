# importing required modules 
import PyPDF2 

# Pede a empresa a que corresponde
empresa = input("Empresa: ")

# Pede os diarios a tirar
diarios = []
diario_input = input("Insira os diarios que pretende tirar: ")
while diario_input:
    diarios.append(diario_input)
    diario_input = input("Insira os diarios que pretende tirar: ")

# Pede os meses a tirar
meses = []
mes_input = input("Insira os meses que pretende tirar (enter para o ano inteiro): ")
if not mes:
    meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
else:
    while mes_input:     
        meses.append(mes_input)
        mes_input = input("Insira os meses que pretende tirar: ")

for diario in diarios:
    for mes in meses:
        # creating a pdf file object 
        pdfFileObj = open('pdf/{} - Extrato diario {} de {}-2019.pdf'.format(empresa, diario, mes), 'rb') 

        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
        # creating a page object 
        pageObj = pdfReader.getPage(-1)

        # creating a pdf writer object for new pdf 
        pdfWriter = PyPDF2.PdfFileWriter()

        # adding page object to pdf writer 
        pdfWriter.addPage(pageObj)

        # new pdf file object 
        newFile = open('pdf/{} - Imprimir diario {} de {}-2019.pdf'.format(empresa, diario, mes), 'wb') 

        # writing watermarked pages to new file 
        pdfWriter.write(newFile) 

        # closing the pdf file object 
        pdfFileObj.close() 
        # closing the new pdf file object 
        newFile.close()
    


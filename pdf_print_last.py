# importing required modules 
import PyPDF2 

meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
diario = ["20","30","60","61","62", "71"]


for diario in diario:
    for mes in meses:
        # creating a pdf file object 
        pdfFileObj = open('pdf/20225 - Extrato diario {} de {}-2019.pdf'.format(diario, mes), 'rb') 

        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
        # creating a page object 
        pageObj = pdfReader.getPage(-1)

        # creating a pdf writer object for new pdf 
        pdfWriter = PyPDF2.PdfFileWriter()

        # adding page object to pdf writer 
        pdfWriter.addPage(pageObj)

        # new pdf file object 
        newFile = open('pdf/20225 - Imprimir diario {} de {}-2019.pdf'.format(diario, mes), 'wb') 

        # writing watermarked pages to new file 
        pdfWriter.write(newFile) 

        # closing the pdf file object 
        pdfFileObj.close() 
        # closing the new pdf file object 
        newFile.close()
    





"""
Getting all the pdf files in the dirctory and change them so only the last page is in the pdf file

Installations:

# pip install PyPDF2
# pip install --user send2trash
"""

import PyPDF2, os, send2trash

# The path where the files are
files_path = "C:\\Users\\Frede\\vs_projects\\diarios_primavera_automation\\pdf"

# Get a list of files in the dir
for files in os.walk(files_path):
    files = list(files[2])
    print(files)


for count,file in enumerate(files):
    file_path = files_path + '\\' + file

    # PDF file object
    pdf_file = open(file_path, 'rb')

    # Creating a pdf reader object 
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Creating a page object with last page of the last object
    last_page = pdf_reader.getPage(-1)

    # Creating a new pdf object
    pdf_writer = PyPDF2.PdfFileWriter()

    # Adding page object to pdf Writer
    pdf_writer.addPage(last_page)

    # open a new pdf file
    new_file_path = files_path + "\\Imprimir - " + file
    new_file = open(new_file_path,  "wb")

    # Writing in the new file
    pdf_writer.write(new_file)

    # Closing files
    pdf_file.close()
    new_file.close()

    # Delete old file
    send2trash.send2trash(file_path)

    # Print new pdf
    os.startfile(new_file_path, "print")
    for pdf in psutil.process_iter():
        if "AcroRd" in str(pdf):
            p.kill()
    
import sys
import os
import PyPDF2

# file = 'BethlehemNH_adf6da59-ca6f-4178-8ddd-33561ef17665.pdf'

thisdir = os.listdir()
for file in thisdir:
    if '.pdf' in file:
        readFile = file
        pdf_object = open(readFile, 'rb')

        pdfReader = PyPDF2.PdfFileReader(pdf_object)

        page1 = pdfReader.getPage(0)

        text = page1.extractText()

        # Convert text  from one string object to list of lines
        lines = text.splitlines()
        header = []
        data = []

        for index, l in enumerate(lines, start=1):
            if (l.endswith((':', '# ', '- '))
                or l == 'Town of '
                or l == 'Parcel Information'
                or l == 'Sale History'
                or l == 'Assessed Value'
                or l.isspace()):
                    continue
            elif l == 'BETHLEHEM':
                address = (l + lines[index]
                    + ' '
                    + lines[index+1]
                    + lines[index+2]
                    + lines[index+3])
                print(address)

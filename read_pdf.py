import csv, sys, os, platform
import PyPDF2

# file = 'BethlehemNH_adf6da59-ca6f-4178-8ddd-33561ef17665.pdf'
system_name = platform.system()

if system_name == 'Darwin':
    thisdir = os.listdir('.')
else:
    thisdir = os.listdir()
# print(thisdir)
JUNK = frozenset({
    'Parcel Information',
    'Town of',
    'Sale History',
    'Property Information -',
    'Assessed Value',
    ',',
    '/',
    'www.cai-tech.com',
    'Bethlehem, NH',
    'Data shown on this report is provided for planning and informational purposes only. The municipality and CAI Technologies',
    'are not responsible for any use for other purposes or misuse or misrepresentation of this report.',
    'Page',
    '1 of 1'
})

MAILING_ADDRESS = frozenset({
    'NH',
    'BETHLEHEM'
})

HEADER_ROW = True

for file in thisdir:
    # Create empty lists for holding headers and cell data.
    header = []
    data = []
    if '.pdf' in file:
        readFile = file
        pdf_object = open(readFile, 'rb')

        pdfReader = PyPDF2.PdfFileReader(pdf_object)

        page1 = pdfReader.getPage(0)

        text = page1.extractText()

        # Convert text  from one string object to list of lines
        lines = text.splitlines()

        with open('bethlehem.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            for index, l in enumerate(lines, start=1):
                line = l.strip()

                # Get rid of Junk
                if ( l.isspace() or line in JUNK ):
                    continue
                # Headers
                if line.endswith((':', '#')):
                    header.append(line)
                # Cells
                else:
                    data.append(line)
            if HEADER_ROW:
                writer.writerow(header)
                HEADER_ROW = False
            writer.writerow(data)

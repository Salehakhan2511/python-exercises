#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HADI
#
# Created:     12/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import PyPDF2
pdffiles =["1pdf","2pdf"]
merge =PyPDF2.PdfMerger()
for filename in pdffiles:
    pdffile= open (filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdffile)
    merge.append(pdfReader)
pdffile.close()
merge.write('merge.pdf')

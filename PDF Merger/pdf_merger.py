# import PyPDF2 library for working with PDF files
import PyPDF2

# specify the paths to the PDF files to be merged
pdfiles=["C:\\Users\\91886\\Desktop\\Python-projects\\PDF Merger\\sample1.pdf",
         "C:\\Users\\91886\\Desktop\\Python-projects\\PDF Merger\\sample2.pdf"]

# create a PdfFileMerger object to merge the PDF files
merger = PyPDF2.PdfFileMerger()

# iterate through the PDF files and append them to the merger object
for filename in pdfiles:
    pdFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)

# close the file object
pdFile.close()

# write the merged PDF file to the disk
merger.write('merged.pdf')
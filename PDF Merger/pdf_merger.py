import pypdf
pdfiles=["sample1.pdf","sample2.pdf"]
merger = pypdf._merger

for filename in pdfiles:
    pdFile=open(filename,'rb')
    pdfReader=pypdf.PdfFileReader(pdfiles)
    merger.append(pdfReader)

pdFile.close()
merger.write('merged.pdf')
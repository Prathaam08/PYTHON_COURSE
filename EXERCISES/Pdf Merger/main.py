from pypdf import PdfWriter

merger = PdfWriter()
for pdf in ["file1.pdf" , "file2.pdf"]:
    merger.append(pdf)
merger.write("Merge-pdf.pdf")
merger.close()
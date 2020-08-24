import PyPDF2
import sys

inputs = sys.argv[1:]

def combiner_pdf(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
	  print (pdf)
	  merger.append(pdf)
	merger.write("combined_pdf.pdf")

combiner_pdf(inputs)

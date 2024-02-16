import argparse
import PyPDF2

def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

parser = argparse.ArgumentParser(description='Merge multiple PDF files into one PDF file.')
parser.add_argument('pdfs', metavar='PDF', type=str, nargs='+', help='the PDF files to merge')
parser.add_argument('output', metavar='OUTPUT', type=str, help='the output PDF file')
args = parser.parse_args()

merge_pdfs(args.pdfs, args.output)

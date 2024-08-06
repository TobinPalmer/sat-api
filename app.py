from flask import Flask

import io
from pdfminer.high_level import extract_text_to_fp

pdf_path = 'math.pdf'
html_output_path = 'output.html'

# Open the PDF file in binary read mode
with open(pdf_path, 'rb') as pdf_file:
    # Open (or create) the output HTML file
    with io.open(html_output_path, 'w', encoding='utf-8') as html_file:
        # Convert PDF to HTML
        extract_text_to_fp(pdf_file, html_file, output_type='html')
print(f"PDF converted to HTML successfully. Check {html_output_path}")

# from pypdf import PdfReader, PdfWriter

# reader = PdfReader("math.pdf")
# writer = PdfWriter()



# Add page 1 from reader to output document, unchanged.
# writer.add_page(reader.pages[2])
# Get the text from page 1 and look for the text "ID: {string}"
# page1text = reader.pages[1].extract_text()
# print(page1text)
#
# # Add page 2 from reader, but rotated clockwise 90 degrees.
# writer.add_page(reader.pages[21].rotate(90))
#
# # Add page 3 from reader, but crop it to half size.
# page3 = reader.pages[3]
# page3.mediabox.upper_right = (
#     page3.mediabox.right / 2,
#     page3.mediabox.top / 2,
# )
# writer.add_page(page3)

# Write to pypdf-output.pdf.
# with open("pypdf-output.pdf", "wb") as fp:
#     writer.write(fp)

# reader = PdfReader("math.pdf")
#
# page = reader.pages[1]
#
# for count, image_file_object in enumerate(page.images):
#     with open(str(count) + image_file_object.name, "wb") as fp:
#         fp.write(image_file_object.data)

# import PyPDF2
#
# reader = PyPDF2.PdfReader('math.pdf')
# print(reader.pages[1].extract_text())
#

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

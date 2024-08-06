from flask import Flask
import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('math.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[1].extract_text())

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

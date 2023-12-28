import PyPDF2

with open('django_for_beginners_4_0.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    pdf_content = ''

    for data in pdf_reader.pages:
        pdf_content += data.extract_text()


print(pdf_content)
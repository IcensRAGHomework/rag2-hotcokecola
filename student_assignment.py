from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

#q1_pdf = "OpenSourceLicenses.pdf"
#q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    
    pyPDFLoader = PyPDFLoader(q1_pdf)
    pyPDFDocument = pyPDFLoader.load()
    #pyPDFDocumentPages = len(pyPDFDocument)
    print(f'The PDF has {len(pyPDFDocument)} pages.')

    # Initialize the CharacterTextSplitter
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    # Access the text of each page and split it into chunks
    for i, document in enumerate(pyPDFDocument):
        pageText = document.page_content
        chunks = splitter.split_text(pageText)
        print(f'Text chunks on page {i + 1}:')
        for chunk in chunks:
            print(chunk)
            print('-' * 20)
 
    return chunks

def hw02_2(q2_pdf):
    pass

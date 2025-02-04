from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

#q1_pdf = "OpenSourceLicenses.pdf"
#q2_pdf = "勞動基準法.pdf"


class Chunk:
    def __init__(self, pdf_name, page_number, chunk):
        self.pdfName = pdf_name
        self.pageNumber = page_number
        self.chunk = chunk

    def __repr__(self):
        return f"PDF Name: {self.pdf_name}, Page Number: {self.page_number}, Chunk: {self.chunk}"

def hw02_1(q1_pdf):
    
    pyPDFLoader = PyPDFLoader(q1_pdf)
    pyPDFDocument = pyPDFLoader.load()
    #pyPDFDocumentPages = len(pyPDFDocument)
    #print(f'The PDF has {len(pyPDFDocument)} pages.')

    # Initialize the CharacterTextSplitter
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    # Access the text of each page and split it into chunks
    chunks = []
    for i, document in enumerate(pyPDFDocument):
        pageText = document.page_content
        splitChunks = splitter.split_text(pageText)
        pageChunk = Chunk(q1_pdf, i + 1, splitChunks)
        chunks.append(pageChunk)

    # Print the chunks
    #for chunk in chunks:
    #    print(chunk)
    #    print('-' * 20)
    
    return pageChunk
    

def hw02_2(q2_pdf):
    pass

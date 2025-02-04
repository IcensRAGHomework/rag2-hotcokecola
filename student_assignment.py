from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)



#q1_pdf = "OpenSourceLicenses.pdf"
#q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    
    pyPDFLoader = PyPDFLoader(q1_pdf)
    pyPDFDocument = pyPDFLoader.load()
    #pyPDFDocumentPages = len(pyPDFDocument)
    #print(f'The PDF has {len(pyPDFDocument)} pages.')

    # Initialize the CharacterTextSplitter
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    chunks = splitter.split_documents(pyPDFDocument)
    lastChunk = chunks[-1]

    return lastChunk

def hw02_2(q2_pdf):
    pass

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

import re
#q1_pdf = "OpenSourceLicenses.pdf"
#q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    
    pyPDFLoader = PyPDFLoader(q1_pdf)
    pyPDFDocument = pyPDFLoader.load()

    # Initialize the CharacterTextSplitter
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    chunks = splitter.split_documents(pyPDFDocument)
    lastChunk = chunks[-1]

    return lastChunk

def hw02_2(q2_pdf):

    loader = PyPDFLoader(q2_pdf)
    pyPDFDocument = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        separators=[r"第[ ]+.*?[ ]*章", r"第[ ]+.*?[ ]*條"],
        #separators=["\n\n"],
        chunk_size=10,
        chunk_overlap=0,
        is_separator_regex=True
    )
    
    chunks = splitter.split_documents(pyPDFDocument)
    numChunks = len(chunks)
    
    count=0
    for i, chunk in enumerate(chunks):
        text = chunk.page_content  # Access the text content of the chunk
        print(f"Chunk {count}:")
        print(text)
        count+=1
        if i == 0:
           continue
        if not text.startswith("第 "):
           numChunks -= 1
           count-=1

 
    #for i, chunk in enumerate(merged_chunks):
    #    print(f"Chunk {i+1}:")
    #    print(chunk)
    #    print("\n" + "-"*50 + "\n")
    

    #print(numChunks) 
    
    return numChunks



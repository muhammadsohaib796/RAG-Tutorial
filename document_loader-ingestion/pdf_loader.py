# PyPDFLoader — Reading PDFs Page by Page

# PDFs are tricky because they can have dozens of pages, images, and formatting.
# PyPDFLoader handles this by splitting each page into its own Document.

# Analogy: If TextLoader reads a whole notebook at once, PyPDFLoader
# tears out each page and hands them to you one by one.

# Best for: Books, research papers, reports, slide decks exported as PDF.

from langchain_community.document_loaders import PyPDFLoader

# Load the PDF — each page becomes a separate Document
pdf_path = "D:\Sohaib\Agentic Ai\RAG TUTORIAL\sample_data\RAG_Masterclass_Guide.pdf"
pdf_loader  = PyPDFLoader(file_path= pdf_path)
pdf_document = pdf_loader.load()

print(f"\nTotal pages loaded: {len(pdf_document)}")
print("=" * 50)


# Loop through the first 3 pages only
# pdf_documents[:3] is called "slicing" — it takes items at index 0, 1, 2
# To see ALL pages, change [:3] to just pdf_documents (remove the slice)
# enumerate() gives us both the index (0, 1, 2) and the document in each iteration
for index, doc in enumerate(pdf_document[:3]):
    print(f"\n--- Page {index + 1} ---")

    # [:200] shows only the first 200 characters (a preview)
    # To see the FULL content of a page, use: print(doc.page_content)
    print(f"Content (first 200 chars): \n{doc.page_content[:300]}...")
    print(f"\nMetadata: {doc.metadata}")


# What just happened?
# Unlike TextLoader (which gave us 1 document), PyPDFLoader gave us 3 documents — one per page!
# Each document's metadata includes page (page number) and source (file path)
# Page numbers start from 0, not 1 (like list indexes in Python)
# Quick comparison:

# Loader	     of Documents	         Why?
# TextLoader	       1	     Entire file = 1 document
# PyPDFLoader	       N	     Each page = 1 document

# =================================================
# Wait — Is PyPDFLoader the ONLY Way to Read PDFs?
# Nope! There are actually several PDF libraries in Python, and LangChain has a loader for each one. 
# They all do the same job (read PDFs), but they have different strengths. Think of it like cars — a sedan. 
# and truck all get you from A to B, but you pick one based on the


# Is your PDF just plain text?
#   └─ YES → PyPDFLoader (simplest, we used this today)

# Does it have complex tables?
#   └─ YES → PDFPlumberLoader or PyMuPDFLoader

# Is it a scanned image (no selectable text)?
#   └─ YES → UnstructuredPDFLoader (with OCR) or AmazonTextractPDFLoader

# Need maximum speed for 1000+ PDFs?
#   └─ YES → PyPDFium2Loader

# Working with Arabic, Chinese, Hindi, or other non-Latin scripts?
#   └─ YES → PyMuPDFLoader (best Unicode support)
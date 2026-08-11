        # Hands-On Part 1: The PDF Explorer
# Time to put it all together! Let's write a reusable function that loads
# any PDF and gives us a nice summary. This is something you'll actually
# use in real projects.


from langchain_community.document_loaders import PyPDFLoader

def explore_pdf(file_path):
    """Load a PDF and print a nice summary of its contents."""

    # Load every page as a separate Document
    pdf_path = r"D:\Sohaib\Agentic Ai\RAG TUTORIAL\sample_data\RAG_Masterclass_Guide.pdf"
    loader = PyPDFLoader(
        file_path = pdf_path
    )
    document = loader.load()

    # Summary header
    print(f"\nPDF: {file_path}")
    print(f"Total Pages: {len(document)}")
    print("="* 60)  # prints 60 equal signs as a visual divider

    # min(3, len(documents)) picks the SMALLER value
    # If the PDF has 50 pages, we show 3. If it has 2 pages, we show 2.
    # This prevents crashing when the PDF has fewer than 3 pages.
    pages_to_show = min(3, len(document))

    # range(pages_to_show) generates numbers: 0, 1, 2 (up to pages_to_show - 1)
    # We use these as indexes to access each document from the list 

    for i in range(pages_to_show):
        doc = document[i]
        print(f"\n---Page {i+1}---")

        # [:300] shows only the first 300 characters as a preview
        # To see the FULL page, replace with: print(doc.page_content)
        print(f"Content preview: {doc.page_content[:300]}")
        print(f"Page metadata: {doc.metadata}")
        print("-" * 60)

        # Show what metadata keys are available
        if document:
                # .keys() returns all the key names from the metadata dictionary
                # list() converts it into a readable list format
            print(f"\nAvaialble metadata keys:{list(document[0].metadata.keys())}")
    return document
    # Try it! Replace 'data/sample.pdf' with your own PDF path if you have one
pdf_docs = explore_pdf("D:\Sohaib\Agentic Ai\RAG TUTORIAL\sample_data\RAG_Masterclass_Guide.pdf")

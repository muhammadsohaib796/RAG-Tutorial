# +----------------------------------+
# |        Document Object           |
# +----------------------------------+
# |  page_content = "actual text"    |  <-- The item inside the box
# |  metadata     = {source, page..} |  <-- The shipping label
# +----------------------------------+

# page_content (str) — The actual text extracted from the file
# metadata (dict) — Extra info: where it came from, page number, author, etc.


from langchain_core.documents import Document

sample_document = Document(
    page_content = "LangChain makes it easy to build AI apps",
    metadata = {
        "source": "manual creation",
        "page": 0,
        "author": "Hope to Skill"
    }
)

# Print what's inside our "box"
print(f"Content: {sample_document.page_content}")
print(f"Metadata: {sample_document.metadata}")
print(f"Type: {type(sample_document)}")


# You can access metadata fields individually
# Using .get() is safer than ['key'] — it won't crash if the key is missing

source = sample_document.metadata.get("source","unknown")
page_number = sample_document.metadata.get("page", -1)
author = sample_document.metadata.get("author", "N/A")

print(f"Source: {source}")
print(f"Page_number: {page_number}")
print(f"Author: {author}")


# TextLoader — Reading Plain Text Files

# The simplest loader. It reads a .txt file and wraps it in a Document.
# Think of it as: "just read the whole file as one block of text."

from langchain_community.document_loaders import TextLoader

# Step 1: Create the loader (tell it which file to read)
text_loader = TextLoader(
    file_path="sample_data/sample.txt",
    encoding="utf-8",
)

# Step 2: Actually load the file — this returns a LIST of Documents
text_documents = text_loader.load()

# Step 3: See what we got
print(f"Documents loaded: {len(text_documents)}")
print(f"\n--- The Text ---")
print(text_documents[0].page_content)
print(f"\n--- The Label (Metadata) ---")
print(text_documents[0].metadata)


# What just happened?
# TextLoader read the entire file and put it in one Document
# The metadata only has source (the file path) — because a text file has no pages or authors
# Notice .load() always returns a list, even if there's only 1 document
# Pattern to remember: Every loader follows the same 2-step dance:
# loader = SomeLoader(source) → docs = loader.load()
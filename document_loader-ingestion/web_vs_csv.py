#       Hands-On Part 2: Loader Showdown — Web vs CSV
# Let's load data from two completely different sources and see how
# LangChain standardizes them into the same format. This is where the
# "universal shipping box" analogy really clicks!


from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import CSVLoader

# --- Load from the Web ---
web_loader = WebBaseLoader(
    web_paths = ["https://en.wikipedia.org/wiki/Retrieval-augmented_generation"]
)

web_docs = web_loader.load()

# --- Load from a CSV ---

# pdf_path = r"D:\Sohaib\Agentic Ai\RAG TUTORIAL\sample_data\RAG_Masterclass_Guide.pdf"

# --- Load from a CSV ---
csv_loader = CSVLoader(
    file_path="sample_data/rag_dataset.csv",
    encoding="utf-8",
)
csv_docs = csv_loader.load()

# --- Compare them side by side ---
print("\nLOADER SHOWDOWN: Web vs CSV")
print("=" * 60)


# :<25 means "left-align and pad to 25 characters wide"
# :>15 means "right-align and pad to 15 characters wide"
# This creates a clean, aligned table in the output

print(f"\n{'Feature':<25} {'Web':>15} {'CSV':>15}")
print(f"{'-' * 25} {'-' * 15} {'-' * 15}")
print(f"{'Document Loaded:':<25} {len(web_docs):>15} {len(csv_docs):>15}")

# .keys() gets all metadata field names, list() makes it printable
web_keys= list[web_docs[0].metadata.keys()]
csv_keys = list[csv_docs[0].metadata.keys()]
print(f"{'metadata keys':<25} {len('web_keys'):>15} {len('csv_keys'):>15}")


# This calculates the average content length across all documents
# sum(...) adds up all the lengths, then we divide by the count
# "for d in web_docs" loops through every document to get its length
web_avg = sum(len(d.page_content) for d in web_docs) / len(web_docs)
csv_avg = sum(len(d.page_content) for d in csv_docs) / len(csv_docs)

# :,.0f formats the number with commas and no decimal places (e.g., 85,432)
print(f"{'Avg content length':<25} {web_avg:>13,.0f}ch {csv_avg:>13,.0f}ch")

print(f"\nWeb metadata keys: {web_keys}")
print(f"CSV metadata keys: {csv_keys}")


# Despite coming from COMPLETELY different sources,
# both have the same .page_content and .metadata structure!

# hasattr() checks if an object has a specific attribute (returns True/False)
# We're proving that BOTH web and CSV documents have the same structure
print("\n--- Web Document (same type!) ---")
print(f"Type: {type(web_docs[0])}")
print(f"Has page_content? {hasattr(web_docs[0], 'page_content')}")
print(f"Has metadata? {hasattr(web_docs[0], 'metadata')}")

print(f"\n--- CSV Document (same type!) ---")
print(f"Type: {type(csv_docs[0])}")
print(f"Has page_content? {hasattr(csv_docs[0], 'page_content')}")
print(f"Has metadata? {hasattr(csv_docs[0], 'metadata')}")

print("\n" + "=" * 60)
print("SAME type, SAME structure, DIFFERENT sources!")
print("This is the power of LangChain's standardized Document object.")



#       What just happened?
# We loaded data from a website and a CSV file — two completely different
# sources — and got back the exact same Document type. The only differences are:

# What's inside page_content (full web page text vs one CSV row)
# What's inside metadata (URL/title vs file path/row number)
# This is the whole point of Document Loaders: no matter where your data comes
# from, your downstream code (text splitting, embeddings, search) stays the same.

# Best practice: Always inspect your loaded data with print() before
# feeding it into a pipeline. Quality varies a lot between sources!
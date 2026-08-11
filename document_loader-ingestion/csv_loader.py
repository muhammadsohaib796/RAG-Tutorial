# CSVLoader — Turning Spreadsheet Rows into Documents

# This is where it gets interesting! CSVLoader turns each row of your CSV
# into a separate Document. Column names become part of the content.

# Analogy: Imagine a filing cabinet. Each drawer (row) becomes its own document,
# with the folder label (column names) included.
# Best for: Product catalogs, customer lists, inventory data, survey results.

from langchain_community.document_loaders.csv_loader import CSVLoader

# Load our bookstore product catalog
csv_path = r"D:\Sohaib\Agentic Ai\RAG TUTORIAL\sample_data\rag_dataset.csv"
csv_loader = CSVLoader(
    file_path= csv_path,
    encoding="utf-8",
)
csv_documents = csv_loader.load()

print(f"\nTotal rows loaded as documents: {len(csv_documents)}")



# Loop through the first 3 rows (products) only
# csv_documents[:3] = slice that takes the first 3 items from the list
# To see ALL rows, remove the [:3] → for index, doc in enumerate(csv_documents):
# enumerate() pairs each item with its position number (0, 1, 2, ...)
for index, doc in enumerate(csv_documents[:3]):
    print(f"\n--- Topic {index + 1} ---")
    print(f"Content:\n{doc.page_content}")   # full content of this row (it's short)
    print(f"Metadata: {doc.metadata}")
    print("-" * 40)  # prints a line of 40 dashes as a visual separator


# What just happened?
# Our CSV had 8 rows, so we got 8 Documents (one per row)
# Each document's page_content contains the column names AND values
# (e.g., product_name: Python Crash Course)
# The metadata tells us the source file and row number

# Notice the difference? A PDF's metadata has page, but a CSV's metadata has row.
# Different loaders provide different metadata — always check what you're getting!
# WebBaseLoader — Grabbing Data from Websites
# What if your data isn't in a file at all — it's on a website?
# WebBaseLoader uses BeautifulSoup to scrape web pages and turn them into Documents.

# Analogy: It's like copying text from a web page and pasting it into a document,
# but automated and at scale.

# Best for: Documentation sites, blog posts, Wikipedia articles, news.
# Not great for: JavaScript-heavy sites (SPAs) — the content may not load.

from langchain_community.document_loaders import WebBaseLoader

# Let's load the Wikipedia page about RAG
web_loader = WebBaseLoader(
    web_paths=["https://en.wikipedia.org/wiki/Retrieval-augmented_generation"],
)
web_documents = web_loader.load()

print(f"\nDocuments loaded: {len(web_documents)}")
print(f"\n--- Metadata ---")
print(web_documents[0].metadata)

# [:500] slices the string to show only the first 500 characters
# Web pages can have 50,000+ characters — too much to print at once!
# To see the FULL page content, use: print(web_documents[0].page_content)

print(f"\n--- Content (first 500 chars) ---")
print(web_documents[0].page_content[:500])


# You can load MULTIPLE web pages at once!
multi_loader = WebBaseLoader(
    web_paths=[
        "https://en.wikipedia.org/wiki/Machine_learning",
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
    ],
)
multi_docs = multi_loader.load()



# This loop goes through EVERY document in multi_docs (no slicing needed — only 2 docs)
# enumerate() gives us the index (0, 1) alongside each document
for index, doc in enumerate(multi_docs):
    # .get() safely reads a key from the metadata dictionary
    # If the key doesn't exist, it returns the fallback value ("Unknown" / "No Title")
    source = doc.metadata.get("source", "Unknown")
    title = doc.metadata.get("title", "No Title")

    # len() counts the total number of characters in the page content
    content_length = len(doc.page_content)

    print(f"\nDocument {index + 1}:")
    print(f"  Title: {title}")
    print(f"  Source: {source}")
    # :, inside the f-string adds commas to large numbers (e.g., 85432 → 85,432)
    print(f"  Content Length: {content_length:,} characters")


#     What just happened?

# Each URL became one Document (the entire page's text)
# Web metadata includes source (URL), title, and sometimes description and language
# The content might look messy — that's because web pages have navigation menus,
# footers, and other text mixed in. We'll learn how to clean this in a later lecture!
# Tip: {content_length:,} adds commas to large numbers (e.g., 85,432 instead of 85432).
# A nice Python trick for readability!
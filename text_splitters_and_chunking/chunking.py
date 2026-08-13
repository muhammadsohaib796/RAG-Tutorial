# Text Splitters & Chunking Strategies

#       The Big Picture
# we learned how to load documents. But here's the problem:

# A 100-page PDF becomes one giant wall of text.
# An LLM can't process that. A search engine can't match against that.
# We need to cut it into smart, bite-sized pieces — that's chunking.

# Chunking is one of the most important decisions in any RAG system.
# Bad chunks = bad retrieval = bad answers, no matter how good your LLM is.

#       What You Will Learn
# #	Topic	Real-World Analogy
# 1	Why we chunk documents	Why you slice a pizza before serving
# 2	Chunk size — the Goldilocks problem	Slices too small or too big
# 3	Overlap — why chunks share text	Pages in a book that repeat the last sentence
# 4	RecursiveCharacterTextSplitter	The smart pizza cutter
# 5	Other splitters	Specialized tools for special jobs
# 6	Metadata preservation	Never lose track of where a chunk came from
# 7	Hands-on: split, compare, choose	Build it yourself!
#   Key Insight: Chunking is where most RAG pipelines silently fail.
#   Master this, and you're ahead of 90% of beginners.
# =============================================================

#       1. Why Do We Chunk Documents?
# The Pizza Analogy
# Imagine you ordered a pizza. The chef hands you the entire uncut pizza.
# You can't eat it like that! You need to cut it into slices.

#       But HOW you cut it matters:

# Too small (tiny squares) — each piece has barely any topping, hard to enjoy
# Too big (half the pizza) — too much to handle at once
# Just right (proper slices) — each slice is a satisfying, complete portion
# Documents work the same way. Here are the 3 reasons we chunk:

#       Reason 1: Context Window Limits
# LLMs can only read a limited amount of text at once (the "context window").
# You can't send 500 pages to an LLM — it will either crash or ignore most of it.

#       Reason 2: Retrieval Precision
# When a user asks a question, you want to find the exact 2-3 paragraphs that
# answer it — not dump 50 pages and hope the LLM figures it out.

#       Reason 3: Semantic Coherence
# Each chunk should contain one complete idea. If you cut in the middle of a
# sentence, the chunk becomes meaningless.

# Bottom line: Bad chunking = bad RAG. No matter how good your LLM is,
# if you feed it garbage chunks, you get garbage answers.
# =============================================================

# First, load our sample article from Lecture 5's data folder

from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="sample_data/nlp_article.txt", encoding="utf-8")
documents = loader.load()

# How big is this document?
# documents[0] gets the first (and only) document from the list
full_text = documents[0].page_content

# len() counts the total number of characters in the string
print(f"\nDocument length: {len(full_text)} characters")

# Rough token estimate: 1 token ~ 4 characters in English
# // is integer division (divides and rounds down, no decimals)
print(f"That's roughly {len(full_text) // 4:,} tokens")

# [:300] shows only the first 300 characters as a preview
# To see the FULL document, use: print(full_text)
print(f"\nFirst 300 characters:")
print(full_text[:300])

#       What just happened?
# We loaded a ~8,000 character article. That's roughly 2,000 tokens.
# This is small enough for most LLMs, but imagine a 200-page PDF —
# that could be 500,000+ characters. Way too much to send at once!

# Quick math: 1 token ~ 4 characters (rough estimate for English).
# GPT-4's context window is ~128K tokens. Claude's is ~200K tokens.
# But just because it fits doesn't mean it's effective — smaller,
# focused chunks always give better retrieval results.


#       2. Chunk Size — The Goldilocks Problem
# Choosing the right chunk size is like Goldilocks and the three bears:
# not too small, not too big, but just right.

#       What Happens at Different Sizes?
# Too Small (<200 chars)	                                    Just Right (500-1500 chars)	                                            Too Large (>2000 chars)
# Example chunk	"NLP is a branch of..."	                     "NLP is a branch of AI that helps computers understand language..."	"NLP is a branch of AI that... [3 pages of text] ...too much noise!"
# Problem	Lost context! Can't understand the idea.	    One complete idea per chunk.	                                            Too much noise in search results.
# Analogy	Pizza cut into tiny squares — no topping per piece	Pizza cut into proper slices — satisfying portions	Half the pizza on one plate — too much to handle
#       The Sweet Spot: 500-1500 Characters
# Chunk Size	Characters	Good For
# Small	200-500	FAQ answers, short paragraphs
# Medium	500-1000	General purpose (good default)
# Large	1000-1500	Technical docs, detailed explanations
# Very Large	1500-2000	Long-form articles, legal documents
# There's no single "correct" size — it depends on your data and use case.
# We'll experiment with different sizes later in this notebook!
# =============================================================


# Let's see what DIFFERENT chunk sizes look like on real text
# We'll manually slice the text to build intuition BEFORE using LangChain

# [:2000] takes only the first 2000 characters of our article for this demo
# To use the full article, replace with: sample_text = full_text
sample_text = full_text[:2000]

# We'll test 3 different chunk sizes to see how they compare
chunk_sizes = [100, 500, 1000]

# This loop runs 3 times — once for each size in the list
for size in chunk_sizes:
    # // is integer division: 2000 // 500 = 4 chunks
    num_chunks = len(sample_text) // size

    # [:size] slices the text from the start to the chunk size
    # If size=100, first_chunk = first 100 characters
    # If size=500, first_chunk = first 500 characters
    first_chunk = sample_text[:size]

    print(f"\n{'=' * 60}")
    print(f"CHUNK SIZE: {size} characters")
    print(f"Number of chunks from 2000 chars: {num_chunks}")
    print(f"First chunk preview:")
    print(f"  '{first_chunk}'")

    # [size-20:size] slices the LAST 20 characters of the first chunk
    # This shows you where exactly the chunk gets cut off
    print(f"  --- ends at: '...{sample_text[size - 20:size]}'")
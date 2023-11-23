
# Keyword and Semantic Search with ReRank

## Introduction

This project leverages advanced techniques in the field of natural language processing (NLP) and semantic search to significantly enhance the quality of search results. It does so by integrating two powerful APIs: Weaviate and Cohere.

## Design

1. **Weaviate API:**
   - Employed for semantic search and keyword-based retrieval.
   - API key and configuration set up as environment variables.
   - Weaviate client instantiated using the Python `weaviate` package.

2. **Cohere API:**
   - Utilized for reranking search results.
   - API key is set up as an environment variable.
   - Cohere client instantiated using the Python `cohere` package.

3. **Python Packages:**
   - `python-dotenv` for managing environment variables.
   - Custom utility functions stored in a `utils.py` file for modular code organization.

### Implementation

1. **Weaviate Integration:**
   - Weaviate is used for both keyword search and dense retrieval.
   - A utility function `dense_retrieval` is defined to perform dense retrieval given a query.

2. **Cohere Integration:**
   - The Cohere API is employed for reranking search results.
   - A utility function `rerank_responses` is defined to rerank a list of responses using the Cohere API.

3. **Keyword Search:**
   - The `keyword_search` function is implemented to perform keyword-based searches using Weaviate.
   - Results are printed with customizable properties and additional information.

4. **Dense Retrieval:**
   - The `dense_retrieval` function is implemented to perform dense retrieval using Weaviate.
   - Results are printed with customizable properties and additional information.

5. **Reranking:**
   - Responses obtained from keyword search or dense retrieval are reranked using the Cohere API.
   - Reranked results are printed for analysis.



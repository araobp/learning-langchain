# Learning LangChain

## My bible

[Marketing 5.0: Technology for Humanity](https://www.wiley.com/en-br/Marketing+5.0%3A+Technology+for+Humanity-p-9781119668510)

As "Marketing 5.0" says, NLP (with LLM) is a core part of Data Driven Marketing.

## Background and Motivation

In the past half year, I have learned NLP with spaCy and SQLite. I am using the NLP skill in my work for marketing these days.

My company has started marketing LLM ["NEC cotomi"](https://www.nec.com/en/press/202404/global_20240424_01.html), so I learn LLM with my NLP skill in this project as a marketer.

## Project Goal

I am a fan of SQLite, so I study in this project how I can use SQLite as a part of RAG.

My final goal is to realize Data Driven Marketing framework with NLP and LLM for promoting LLM in the market. The framework will not be included in this project.

## Code

### [rag](./rag)

Test LangChain's RAG capabilities with OpenAI.

### [spacy](./spacy)

Test spaCy's built-in embedding capabilities.

### [keyphrase](./keyphrase)

Use ChromaDB for keyphrase similality search with textacy.
This code use neither LangChain nor OpenAI.

## OpenAI API

https://platform.openai.com

## Embeddings

I test OpenAI, spaCy and Sentence Transformers to generate embeddings.

Note: spaCy's "en-core-web-lg" and ""ja-core-news-lg"" seems to output embeddings the size of 300 dimensions. On the other hand, "en-core-web-trf" does not seem to support embeddings.

## VectorDB

[Chroma](https://www.trychroma.com/)

I want to use Chroma and my original GraphDB to achive my goal for Data Driven Marketing.

## My original GraphDB

I have already developed GraphDB with SQLite and networkx on my own at work:
- My original schema to store graph entities (nodes).
- My original SQL to generate edges on a certain condition (i.e., dependency between nodes).
- Run Graph Theory on the generated network with networkx.

The GraphDB is very useful for my work, especially useful for automatic market segmentation.

The GraphDB is not included in this project.

## Reference

- [LangChain完全入門](https://github.com/harukaxq/langchain-book)
- [Chainlit](https://github.com/Chainlit/chainlit)

# Learning LangChain

(Work in progress)

## My bible

[Marketing 5.0: Technology for Humanity](https://www.wiley.com/en-br/Marketing+5.0%3A+Technology+for+Humanity-p-9781119668510)

As "Marketing 5.0" says, NLP (with LLM) is a core part of Data Driven Marketing.

## Background and Motivation

I used to be a network engineer: IP Telephony, routers and switches. I also worked on SDN that ran on a kind of Graph DB.

In the past half year, I have learned NLP with spaCy and SQLite. I am using the NLP skill in my work for marketing these days.

My company has started marketing LLM ["NEC cotomi"](https://www.nec.com/en/press/202404/global_20240424_01.html), so I learn LLM with my NLP skill in this project as a marketer.

## Project Goal

I am a fan of SQLite, so I study in this project how I can use SQLite as a part of RAG.

My final goal is to realize Data Driven Marketing framework with NLP and LLM for promoting LLM in the market. The framework will not be included in this project.

My another goal is to run a tiny LLM (Llama) with LangChain locally to simulate a on-premise environment where very high security and privacy is required.

## Code

### [rag](./rag)

Test LangChain's RAG capabilities with OpenAI.

I conclude that the document sources are much more important than RAG.

### [spacy](./spacy)

Test spaCy's built-in embedding capabilities.

I conclude that the built-in embedding capabilities are not useful in my work.

### [keyphrase](./keyphrase)

Use ChromaDB for keyphrase similality search with textacy. This code use neither LangChain nor OpenAI.

I conclude that Sentence Transformers are useful in my work.

## OpenAI API

https://platform.openai.com

## Embeddings

I test OpenAI, spaCy and Sentence Transformers to generate embeddings.

Note: spaCy's "en-core-web-lg" and ""ja-core-news-lg"" seems to output embeddings the size of 300 dimensions. On the other hand, "en-core-web-trf" does not seem to support embeddings.

## VectorDB

[Chroma](https://www.trychroma.com/)

I want to use Chroma and my original GraphDB to achive my goal for Data Driven Marketing.

## My original GraphDB (private project)

In a real world, SQL DB needs to coexist with GraphDB and VectorDB to meet various demands from marketing teams.

I have already developed GraphDB with SQLite and networkx on my own:
- My original schema to store graph entities (nodes).
- My original SQL to dynamically generate triplets on a certain condition (i.e., edges between nodes with dependencies).
- Run Graph Theory on the generated network to generate a sub graph.

```
     Network Graph A    Network Graph C
               |           |   <- - - Connect networks with semantic search
              Network Graph B
```

The GraphDB is not included in this project.

## Reference

- [LangChain with NetworkX](https://python.langchain.com/v0.1/docs/integrations/graphs/networkx/)
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Run LLMs locally](https://python.langchain.com/v0.1/docs/guides/development/local_llms/)

## 参考

- [LangChain完全入門](https://github.com/harukaxq/langchain-book) ==> NLPのスキルあればサッとRAGを理解出来る。そういう意味で良書。
- [【考察】RAGはマニュアル人間で、ファインチューニングは新卒育成？](https://leapwell.co.jp/tech_column/blog-finetuning-vs-rag) ==> VERY GOOD!
- [「コンテンツの構造化が大変！?」顧客接点へのAI導入の課題はRAG技術で解決](https://blog.cba-japan.com/rag/) ==> 私が日々オーバーワークになっている理由がこれ。構造化が異常に大変！
- [ローカル で Llama 2 + LangChain の RetrievalQA を試す](https://note.com/npaka/n/n3164e8b24539)
- [生成 AI（LLM）のビジネス適用の潮流 ](https://www.dir.co.jp/report/consulting/dx/20240318_024297.pdf)


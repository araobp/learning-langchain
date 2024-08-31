# How to create Custom Chat Model

Reference: https://python.langchain.com/v0.2/docs/how_to/custom_chat_model/

企業の中で仕事していると、セキュリティーや監査の理由上、直接、OpenAI等のAPIへアクセスすることが出来ない場合が多い。そういう環境でもLangChainを使いたい。

まずは、OpenAIのREST APIを企業の中で提供される独自APIに見立てて、これをLangChainへ組み込んでみる。

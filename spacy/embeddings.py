# Reference: https://python.langchain.com/v0.2/docs/integrations/text_embedding/spacy_embedding/

from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings

embedder_en = SpacyEmbeddings(model_name="en_core_web_lg")
embedder_ja = SpacyEmbeddings(model_name="ja_core_news_lg")

texts_en = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!",
    "Bright vixens jump; dozy fowl quack.",
]

texts_ja = [
    "今日の天気は晴れで、気温も過ごしやすいです。午後には少し曇るかもしれませんが、雨の心配はないでしょう。",
    "昨夜、新しいレストランに行ってみました。料理はとても美味しく、サービスも素晴らしかったので、また訪れたいと思います。",
    "最近、毎朝ジョギングを始めました。運動すると気分がすっきりし、1日を元気に過ごすことができます。",
    "新しいプロジェクトのために、チームでブレインストーミングを行いました。たくさんのアイディアが出て、今後の展開が楽しみです。"
]

embeddings_en = embedder_en.embed_documents(texts_en)
#for i, embedding in enumerate(embeddings):
#    print(f"Embedding for document {i+1}: {embedding}")
embeddings_ja = embedder_ja.embed_documents(texts_ja)

QUERY_EN = "Quick foxes and lazy dogs."
QUERY_JA = "今日はレストランで食事する予定"

query_embedding_en = embedder_en.embed_query(QUERY_EN)
print(f"Embedding for query: {query_embedding_en}")
print(len(query_embedding_en))

query_embedding_ja = embedder_ja.embed_query(QUERY_JA)
print(f"Embedding for query: {query_embedding_ja}")
print(len(query_embedding_ja))

import chromadb
chroma_client = chromadb.Client()



collection = chroma_client.create_collection(name="metrix")
print(chroma_client.list_collections())




import os
import faiss
import numpy as np
import fitz
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
 
# -------------------- Configuration --------------------
PDF_FOLDER = "resumes"
FAISS_INDEX_FILE = "resume_index.faiss"
INDEX_DATA_FILE = "resume_chunks.npy"
MONGO_URI = "mongodb+srv://maheswarareddysirasani:NwCOfEtBzPT9uT7e@cluster0.jpwjh1o.mongodb.net/?retryWrites=true&w=majority&tls=true"
DB_NAME = "resume_manager"
COLLECTION_NAME = "resumes"
 
# -------------------- Initialization --------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # ~384 dimensional output
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
resume_collection = db[COLLECTION_NAME]
embedding_dim = 384
index = faiss.IndexFlatL2(embedding_dim)
index_data = []
 
# -------------------- Index Management --------------------
def load_index():
    global index, index_data
    if os.path.exists(FAISS_INDEX_FILE):
        index = faiss.read_index(FAISS_INDEX_FILE)
    if os.path.exists(INDEX_DATA_FILE):
        index_data = np.load(INDEX_DATA_FILE, allow_pickle=True).tolist()
 
def save_index():
    faiss.write_index(index, FAISS_INDEX_FILE)
    np.save(INDEX_DATA_FILE, index_data)
 
# -------------------- PDF & Text Utils --------------------
def load_pdf_text(pdf_path):
    pdf_document = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in pdf_document])
 
def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
 
def get_embeddings(text):
    return embedding_model.encode(text)
 
# -------------------- Indexing --------------------
def index_resumes():
    global index_data
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            if resume_collection.find_one({"_id": filename}):
                print(f"Skipping: {filename} - already indexed")
                continue
            text = load_pdf_text(os.path.join(PDF_FOLDER, filename))
            chunks = chunk_text(text)
            for chunk in chunks:
                embedding = get_embeddings(chunk)
                index.add(np.array([embedding], dtype="float32"))
                index_data.append({"_id": filename, "chunk": chunk})
            resume_collection.insert_one({"_id": filename, "text": text})
            print(f"Indexed the resume {filename}")
    save_index()
 
# -------------------- Querying --------------------
def query_resume(query):
    if index.ntotal == 0 or len(index_data) == 0:
        print("No resumes are indexed. Please use Option 1.")
        return
    query_vector = get_embeddings(query)
    D, I = index.search(np.array([query_vector], dtype="float32"), 3)
    print("\nTop Matches:\n")
    for idx in I[0]:
        print(f"Resume: {index_data[idx]['_id']}\nSnippet: {index_data[idx]['chunk'][:300]}...\n")
 
# -------------------- Main CLI --------------------
def main():
    load_index()
    while True:
        print("\nGPT-Free Resume QnA")
        print("1. Process the Resumes in Resume Folder")
        print("2. Ask Questions")
        print("3. Exit")
        choice = input("Select an Option: ")
        if choice == "1":
            index_resumes()
        elif choice == "2":
            query = input("Ask your question: ")
            query_resume(query)
        elif choice == "3":
            print("Goodbye... See you again.")
            break
        else:
            print("Invalid user input. Please try again.")
 
if __name__ == "__main__":
    main()
 
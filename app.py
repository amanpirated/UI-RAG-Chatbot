#------------------------------------------Importing all required libraries---------------------------------------
import numpy as np
import faiss
import streamlit as st  # type: ignore[import]

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from google import genai

#--------------------------------------------------Gemini API------------------------------------------------------------

API_KEY="AQ.Ab8RN6IKqEqA5ba6C6M_1mxltGFyrxIe1jomprjx4i4az7Ci5A"
client=genai.Client(api_key=API_KEY)

#------------------------------------------------- Load RAG System ---------------------------------------------------

@st.cache_resource
def load_rag_system():
    #Reading text from pdf

    reader=PdfReader("C:\\UIChatbot\\data\\notes.pdf")
    text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text + "\n"
    #Chunking

    chunkSize=500
    chunks=[]
    for i in range(0,len(text),chunkSize):
        chunks.append(text[i:i+chunkSize])
    #Embedding Model 

    embedding_model=SentenceTransformer("all-MiniLM-L6-V2")
    embeddings=embedding_model.encode(chunks)
    #FAISS

    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )
    return embedding_model, index, chunks
embedding_model,index,chunks=load_rag_system()

#---------------------------------------------Rag Function---------------------------------------------

def ask_rag(query):
    query_embedding=embedding_model.encode([query])
    distance,indices=index.search(
        np.array(query_embedding,dtype=np.float32),
        k=3
    )
    retrieved_chunks=[]
    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])
    context="\n\n".join(retrieved_chunks)
    prompt=f"""
Answer only from the provided context

Context:{context}

Question:{query}
"""
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
#----------------------------------User Interface------------------------------------
st.title("PDF RAG Chatbot")
st.write("Ask Questions from your Pdf document")

query=st.text_input(
    "Enter your question"
)
if st.button("Ask"):
    if query:
        with st.spinner("Searching...."):
            answer = ask_rag(query)
        st.success("Answer")
        st.write(answer)


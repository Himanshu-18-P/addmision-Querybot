from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
import os


class PrepareData:

    def __init__(self):
        self.pdf_loader = None
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'})
        self.db_path = None
        self.user_prompt_db = None
    

    def set_pdf_path(self , pdf_path , db_path ):
        self.pdf_loader = PyPDFLoader(pdf_path)
        self.db_path = db_path
        return 
    
    def load_create_emb_fassi(self ,build_new = False):
        documents = self.pdf_loader.load_and_split()
        print(documents[0])
        if build_new or not(os.path.exists(self.faiss_db_path)):
            vectorstore = FAISS.from_documents(documents=documents, embedding=self.embeddings)
            vectorstore.save_local(self.db_path)
        self.db = FAISS.load_local(self.db_path, self.embeddings, allow_dangerous_deserialization=True)
        return
    
    def load_create_emb_chroma(self , build_new = False):
        documents = self.pdf_loader.load_and_split()
        documents[0]
        if build_new or not(os.path.exists(self.db_path)):
            vector_store = Chroma(
                collection_name="example_collection",
                embedding_function=self.embeddings,
                persist_directory=self.db_path,  # Where to save data locally, remove if not neccesary
              )
        self.db = Chroma(persist_directory=self.db_path, embedding_function=self.embeddings)
        return


    
    def retrive_similer_docs_using_fassi(self , question , path):
        if not self.user_prompt_db:
            self.user_prompt_db = FAISS.load_local(path, self.embeddings, allow_dangerous_deserialization=True)
        retireved_results= self.user_prompt_db.similarity_search(question , k=3)
        content = ''
        for result in retireved_results:
            content += result.page_content
        return content
    
    def retrive_similer_docs_using_chroma(self , path , question):
        if not self.user_prompt_db:
            self.user_prompt_db = Chroma(persist_directory=path, embedding_function=self.embeddings)
        retireved_results= self.user_prompt_db.similarity_search(question , k=5)
        content = ''
        for result in retireved_results:
            content += result.page_content
        return content
    

    

if __name__ == '__main__':
    obj = PrepareData()
    pdf_path = '../system_prompt/python_fynd.pdf'
    db_path = 'fassi_db/fynd'
    obj.set_pdf_path(pdf_path , db_path)
    # obj.load_create_emb_chroma(True)
    print(obj.retrive_similer_docs_using_fassi('fassi_db/fynd' , 'what is week 4 syllabus'))
    print('done')


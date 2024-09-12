from core.genrate_response import * 
from core.create_prompt import * 


class ProcessAPI:

    def __init__(self) -> None:
        self.gen_response = GenerateResponse()
        self.data = PrepareData()


    def process(self ,question):
        context = self.data.retrive_similer_docs_using_fassi(question , 'core/create_prompt/fassi_db/fynd')
        answer = self.gen_response.process_question(question , context)
        return answer        
    

if __name__ == '__main__':
    print('done')
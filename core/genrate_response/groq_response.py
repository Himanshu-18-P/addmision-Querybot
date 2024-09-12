from groq import Groq
import os 
from dotenv import load_dotenv
from core.system_prompt.prompt import *

load_dotenv('.env.secrets')

class GenerateResponse:

    def __init__(self):
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'),)

    
    def chat_complition(self , question , context):
        chat_completion = self.client.chat.completions.create(
            #
            # Required parameters
            #
            messages=[
                # Set an optional system message. This sets the behavior of the
                # assistant and can be used to provide specific instructions for
                # how it should behave throughout the conversation.
                {
                    "role": "system",
                    "content": groq_prompt['groq'] + 'context for answer' + context
                },
                # Set a user message for the assistant to respond to.
                {
                    "role": "user",
                    "content": question,
                }
            ],

            # The language model which will generate the completion.
            model="llama3-8b-8192",
            temperature=0.5,

            # The maximum number of tokens to generate. Requests can use up to
            # 32,768 tokens shared between prompt and completion.
            max_tokens=1024,

            # Controls diversity via nucleus sampling: 0.5 means half of all
            # likelihood-weighted options are considered.
            top_p=1,

            # A stop sequence is a predefined or user-specified text string that
            # signals an AI to stop generating content, ensuring its responses
            # remain focused and concise. Examples include punctuation marks and
            # markers like "[end]".
            stop=None,

            # If set, partial message deltas will be sent.
            stream=False,
        )
    
        # Print the completion returned by the LLM.
        return (chat_completion.choices[0].message.content)
    

    def process_question(self , query , text):

        if query == 'start':
            return groq_prompt['start_response']
        
        else:
            response = self.chat_complition(query , text)
            return response 
        
if __name__ == '__main__':
    res = GenerateResponse()
    # response = res.process_question('tell me about this course' , '' )
    # print(response)

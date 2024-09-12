from start import *
from flask import Flask , request
# print(GenerateResponse().chat_complition('tell me about course' , 'python course of 6 month'))
# print(ProcessAPI().process('week4 objective please tell me'))


def create_app():

    app = Flask(__name__)        

    @app.route('/')
    def index():
        return {'message' : "hare krishna"}
    
    @app.route('/api/process' , methods = ['POST'])
    def process():
        data = request.json
        print(data)
        question = data['question']
        answer = init.process.process(question)
        return {'response' : answer}
    
    return app 

if __name__ == '__main__':
    init = Intialization()
    app = create_app()
    app.run(debug =True)
from flask import Flask, request, make_response, jsonify, json


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    env = app.config['env']
    #response.status_code = 404
    #return make_response('',404)
    return f"<h2>Learning of CI CD pipeline with Flask + Pytest + Docker + Docker Hub + Github workflow + AWS EC2. </h2><p><strong>Env: </strong><i>{env}</i> server </p>"

@app.route('/requirements', methods=['GET'])
def requirements():
     req_dct = {}
     with open('requirements.txt', 'r') as req_list:
          buff = req_list.read()
          buff = buff.split('\n')
          req_dct = {item.split('==')[0]:item.split('==')[1] for item in buff}
          req_list.close()
     rsp = app.response_class(
         response = json.dumps(req_dct),
         mimetype = 'application/json',
         status = 200
     )
     return rsp

if __name__ == '__main__':
    app.config['env'] = 'Development'
    app.run(host='0.0.0.0',port=8000, debug=True)
else:
    app.config['env'] = 'Production'

from flask import Flask, request, render_template
from flask_cors import CORS

from flask import Response


app = Flask(__name__,static_folder="/")
CORS(app)

VERIFY_TOKEN = "zzzz"

@app.route('/webhook', methods=['GET','POST'])
def index():
    if request.method=="GET":
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if(mode and token):
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                return Response(challenge, status=200, mimetype='application/json')
            else:
                return Response('403 Forbidden', status=403, mimetype='application/json')
        
    else:
        
        object=request.json['object']
        L_entry=request.json['entry']
        if object=="page":
            for entry in L_entry:
                webhook_event = entry['messaging'][0]
                print(webhook_event)
                
            return Response('EVENT_RECEIVED', status=200, mimetype='application/json')
        else:
            return Response('404 Not Found', status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3089)


# curl -H "Content-Type: application/json" -X POST "localhost:3089/webhook"

#  -d '{"object": "page", "entry": [{"messaging": [{"message": "TEST_MESSAGE"}]}]}'
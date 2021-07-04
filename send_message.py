import requests
token_page = ''
psid = '4123218751106096'
message = 'hellio cac pan'

dataPost = {
    "recipient":{
        "id":psid
    },
    "message":{
        "text":message
    }
}

url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%token_page
res = requests.post(url,json=dataPost).json()
print(res)
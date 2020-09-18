import requests
from flask import Flask, render_template, request
from pprint import pprint
app = Flask(__name__)

token = '1028060933:AAGL7GI4bFec6NcbFqUXda3QglXapya0SEQ'
api_url = f'https://api.telegram.org/bot{token}'
naver_client_id = 'yZLp1gPOjrM5BFTqAU54'
naver_client_secret = 'schgubwIiF'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

# 1. 사용자의 입력 메시지를 받아서 저장
@app.route('/send')
def send():
    text = request.args.get('message')

# 2. getUpdates 내역 가져오기
    update_url = f'{api_url}/getUpdates'
    response = requests.get(update_url).json()

# 3. 사용자 chat_id 찾기
    chat_id = response.get('result')[0].get('message').get('chat').get('id')

# 4. sendMessage 메서드를 이용해서 텔레그램에 전송.
    message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    
    return render_template('send.html')


@app.route('/telegram', methods=['post'])
def telegram():
    telegram_respones = request.get_json()
    if telegram_respones.get('message') is not None:
        chat_id = telegram_respones.get('message').get('from').get('id')
        text = telegram_respones.get('message').get('text')

        #번역 기능
        if text[0:4] == '/번영 ':
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'        
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }

            data = {
                'source' : 'ko',
                'target' : 'en',
                'text' : text[4:]
            }
            papapgo_response = requests.post(papago_url, headers=headers, data=data)
            papago_text = papapgo_response.json().get('message').get('result')
            text = papago_text['translatedText']
        
        if text[0:4] == '/번한 ':
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'        
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }

            data = {
                'source' : 'en',
                'target' : 'ko',
                'text' : text[4:]
            }
            papapgo_response = requests.post(papago_url, headers=headers, data=data)
            papago_text = papapgo_response.json().get('message').get('result')
            text = papago_text['translatedText']
        
        requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}') 





    #### telegram 한테 send message하라고 요청을 보내는 것.
    # requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')    

    

    return '', 200







if __name__ == '__main__':
    app.run(debug=True)
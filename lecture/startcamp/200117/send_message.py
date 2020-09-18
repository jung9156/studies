import requests
from pprint import pprint
# 1. 기본 값 설정
token = '1028060933:AAGL7GI4bFec6NcbFqUXda3QglXapya0SEQ'
# chat_id = '1026407595'
api_url = f'https://api.telegram.org/bot{token}'

# 2. getUpdates 요청하기
update_url = f'{api_url}/getUpdates'
response = requests.get(update_url).json()
# pprint(response)

# 3. 응답 결과에서 내 chat_id 찾기
chat_id = response.get('result')[0].get('message').get('chat').get('id')

# 4. 보낼 메세지 작성
text = '안녕하세요'

# 5. 텔레그램으로 메세지 보내기
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)

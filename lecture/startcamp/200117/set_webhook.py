import requests

token = '1028060933:AAGL7GI4bFec6NcbFqUXda3QglXapya0SEQ'
api_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'jung9156.pythonanywhere.com'
set_webhook_url = f'{api_url}/setWebhook?url={ngrok_url}/telegram'

respones = requests.get(set_webhook_url)
print(respones.text)
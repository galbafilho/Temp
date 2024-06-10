import requests

API_KEY = ''
cidade = 'Ibiapina'
url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

resposta = requests.get(url)
dados = resposta.json()

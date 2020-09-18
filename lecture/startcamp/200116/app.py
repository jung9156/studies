import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta
from flask import Flask, render_template, request
app = Flask(__name__)


url = 'https://search.naver.com/search.naver?query=lotto'        
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
lotto = data.find_all('num_box')
            
lotto_text = lotto

print(lotto)
from flask import request, jsonify, Blueprint, make_response
import requests
from bs4 import BeautifulSoup

mod = Blueprint('news', __name__, url_prefix='news')

@mod.route('/query', methods=["GET"])
def query_content():
    link = "https://zh.wikipedia.org/wiki/%E8%97%8D%E7%99%BD%E5%90%88%E4%BD%9C#%E8%97%8D%E7%99%BD%E5%90%88%E4%BD%9C%E7%9A%84%E6%8E%A2%E8%A8%8E%E8%88%87%E9%81%8E%E7%A8%8B"
    response = requests.get(link)
    soup = BeautifulSoup(response.content.decode(), 'html.parser')
    description = soup.get_text()
    return description



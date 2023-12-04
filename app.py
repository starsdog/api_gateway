from flask import Flask,Blueprint
import api.api_news as api_news

app = Flask(__name__)

app.register_blueprint(api_news.mod, url_prefix='/news')

if __name__ == '__main__':
    app.debug=True
    app.run(port=8080, host='0.0.0.0')

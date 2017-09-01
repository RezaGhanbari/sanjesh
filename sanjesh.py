from flask import Flask
import requests
from lxml import etree
from src.grabber import *
import re

app = Flask(__name__)




@app.route('/')
def index():
    src = grabber()

    root = etree.fromstring(src)[0][3][0]
    content = etree.tostring(root)
    return re.sub('<[^<]+?>', '', content)


if __name__ == '__main__':
    app.run(debug=False)

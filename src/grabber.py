import requests

def grabber():
    url = 'http://sanjesh.org/rss/rss.aspx?id=2'
    response = requests.get(url)
    return response.content


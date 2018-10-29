import proxy
import requests

url = 'https://api.telegram.org/bot'
TOKEN_TELEGRAM = open("DATA_API.txt", "r").read()


def get_updates_json(request, prx):
    response = requests.get(request + TOKEN_TELEGRAM + '/getUpdates',  proxies=proxy.OpenProxy(prx))
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def writetofilelastmassages(file1):
    open(file1, "w").write(str(get_updates_json(url, "proxy.txt")))
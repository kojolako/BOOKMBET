import requests

url = "https://api.telegram.org/bot"
TOKEN_TELEGRAM = "0"

def get_updates_json(request):  
    response = requests.get(request + TOKEN_TELEGRAM + '/getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

TOKEN_TELEGRAM = input("TOKEN")

upd = open("upd.txt", "w")

upd.write(str(get_updates_json(url)))
print(get_updates_json(url))

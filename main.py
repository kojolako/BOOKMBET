import requests

url = "https://api.telegram.org/bot"
TOKEN_TELEGRAM = open("DATA_API.txt", "r").read()

proxies = open("proxy.txt", "r")

prx = {}
with open("proxy.txt", "r") as file:
    for line in file:
        key, value = line.split()
        prx[key] = value

print(prx)


def get_updates_json(request):
    response = requests.get(request + TOKEN_TELEGRAM + '/getUpdates',  proxies=prx)
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]



upd = open("upd.txt", "w")

upd.write(str(get_updates_json(url)))
print(get_updates_json(url))



import requests
import proxy
url = "https://ua1xbet.com"

r = requests.get(url, proxies=proxy.OpenProxy("proxy.txt"))
print(r.text)
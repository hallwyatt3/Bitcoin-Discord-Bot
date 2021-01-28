from discord_webhook import DiscordWebhook
import time
from coinbase_price import price
from time import sleep
import math

webhook_url = '<insert webhook url>'

rate = price()

class Webhook:
    def package_message(self,message):
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()

    def tell_time(self):
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        second = time.localtime().tm_sec
        time_fmtd = f'{hour}:{minute}:{second}'
        return time_fmtd

    def create_message_bitcoin(self):
        return f'Bitcoin is now at ${price()} @ {self.tell_time()}'

    def round_to_thousand(self, number):
        base = 1000
        return math.floor(number/base)*base
    
    def bitcoin_significant(self):
        global rate
        sleep(60)
        rate2 = price()
        #if rate and current price() do not equal each other when rounded to the 
        #nearest thousand, that means the number has crossed a 
        #threshold
        print(f'Rate-1 is {rate} and rate-2 is {rate2}', end='\r')
        if self.round_to_thousand(rate) != self.round_to_thousand(rate2):
            print(f'Message sent to Discord Chat. ${rate}')
            rate = rate2
            return True
        else:
            rate = rate2

    def function_main(self):
        while True:
            if self.bitcoin_significant():
                message = wh.create_message_bitcoin()
                wh.package_message(message)
                sleep(10)


wh = Webhook()
wh.function_main()

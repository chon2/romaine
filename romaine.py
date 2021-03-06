import sensor
from prom_pg_client import push
import time
import telegram
import requests
import traceback

from raven import Client

client = Client('https://063ad6fa9d854929968e523ad81d0db2:c3c6144b11ed449584aedcd4a802c499@sentry.io/1264249')

# Intervals of about 2 seconds or less will eventually hang the DHT22.
INTERVAL = 60
DHT22_PIN_NUM = 4

telegram_bot_token = "616109347:AAGBMYhjA9GY_Oehd--3lo6bTdqkrgFSwqU"
chat_id = 476794024

def get_ngrok_status():
    resp = requests.get("http://localhost:4040/api/tunnels")
    return resp.json()

def send_telegram(message, chat_id=chat_id):
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_message(chat_id, message)

if __name__ == '__main__':
    ngrok_status = get_ngrok_status()

    try:
        send_telegram(ngrok_status)
    except Exception:
        traceback.print_exc()

    pi = sensor.start_pigpio()
    dht22 = sensor.start_dht22(pi, DHT22_PIN_NUM)
    sensor.read_dht22(dht22)
    time.sleep(.03)
    next_reading = time.time()
    while True:
        try:
            sensor.read_dht22(dht22)
            humidity = dht22.humidity()
            temperature = dht22.temperature()
            print("t:{}, h:{}%".format(temperature, humidity))
            push.to_gateway('area 1', temperature, humidity, job='romaine')
        except KeyboardInterrupt :
            break 
        except Exception :
            traceback.print_exc()
        finally:
            dht22.sensor_resets()
            next_reading += INTERVAL
            time.sleep(next_reading-time.time())
           
    sensor.stop_dht22(dht22)
    sensor.stop_pigpio(pi)
    print("terminated this program...")

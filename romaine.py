import sensor
from prom_pg_client import push
import time
import telegram
import requests

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
    send_telegram(ngrok_status)

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
            dht22.sensor_resets()
            next_reading += INTERVAL
            time.sleep(next_reading-time.time())
        except KeyboardInterrupt :
            break 
    sensor.stop_dht22(dht22)
    sensor.stop_pigpio(pi)
    print("terminated this program...")

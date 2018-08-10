import sensor
from prom_pg_client import push
import time

# Intervals of about 2 seconds or less will eventually hang the DHT22.
INTERVAL = 60
DHT22_PIN_NUM = 4

if __name__ == '__main__':
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


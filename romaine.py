import sensor
from prom_pg_client import push

if __name__ == '__main__':
    sensor.start_pigpid()
    sensor.start_dht22()

    while True:
        try:
            humidity = sensor.humidity()
            temperature = sensor.temperature()
            push.to_gateway('area 1', temperature, humidity, job='romaine')
        except KeyboardInterrupt :
            pass

    print("terminate this program...")
    sensor.stop_dht22()
    sensor.stop_pigpio()

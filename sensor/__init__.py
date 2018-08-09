import pigpio

from time import sleep

# this connects to the pigpio daemon which must be started first
from sensor import DHT22

def start_pigpio():
    return pigpio.pi()

def start_dht22(pi, pin_num):
    return DHT22.sensor(pi, pin_num)

def read_dht22(sensor):
    sensor.trigger()
    sleep(.03) # Necessary on faster Raspberry Pi's
    #print('{:3.2f}'.format(sensor.humidity() / 1.))
    #print('{:3.2f}'.format(sensor.temperature() / 1.))


def stop_dht22(sensor):
    sensor.cancel()

def stop_pigpio(pigpio):
    pigpio:memoryview.stop()

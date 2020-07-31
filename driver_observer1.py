from observer1 import Publisher, Subscriber
import bme280
import smbus2
from time import sleep


port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

def read_all():
    data = bme280.sample(bus,address)
    measurements = [data.humidity,data.pressure,data.temperature]
    return measurements

publisher = Publisher()
Alexa = Subscriber('Alexa Interface')
Webpage = Subscriber('GitHub Pages')

publisher.register(Alexa)
publisher.register(Webpage)
measurements = read_all()
publisher.dispatch(measurements)

from observer2 import Publisher, Subscriber
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

publisher = Publisher(["humidity", "pressure", "temperature"])
Alexa = Subscriber('Alexa Interface')
Visualization = Subscriber('Python Graph')

publisher.register("humidity", Alexa)
publisher.register("pressure", Alexa)
publisher.register("temperature", Alexa)
publisher.register("temperature", Visualization)

data = read_all()
humidity = str(data[0])
pressure = str(data[1])
temperature = str(data[2])
publisher.dispatch("humidity", "Humidity = " + humidity)
publisher.dispatch("pressure", "Pressure = " + pressure)
publisher.dispatch("temperature", "Temperature = " + temperature)

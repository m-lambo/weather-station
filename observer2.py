class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{} got message '{}'".format(self.name,message))

class SubscriberDB:
    def __init__(self, name, connection, cursor):
        self.name = name
        self.connection = connection
        self.cursor = cursor
    def insert(self, message):
        print("Updated table " + self.name + " on MariaDB Platform.")
        self.cursor.execute("INSERT INTO weather.ATMOSPHERIC_MEASUREMENTS(HUMIDITY, PRESSURE, TEMPERATURE) VALUES (?, ?, ?)",(message[0], message[1], message[2]))

# class SubscriberVisualization(Subscriber):
  # import python graph library
  #  def __init__(self, name):
   #     Subscriber.__init__(self, name)
    # def graphicallyDisplay(self, message):
  # graph data points

 #class SubscriberAlexa(Subscriber):
  # technically will subscriber the MQTT broker I presume
  #  def __init__(self, message):
    #    Subscriber.__init__(self, message):
   # def transferDataToBroker(self, message):
  # send measurements from python to broker
class Publisher:
    def __init__(self):
        self.subscribers = dict()
    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback
    def unregister(self, who):
        del self.subscribers[who]
    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)
            

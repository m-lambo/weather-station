class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{} got message '{}'".format(self.name,message))

class SubscriberDB(Subscriber):
import database

	def __init__(self, name):
		Subscriber.__init__(self, name)
  # construct database object
  # initialize object to correspond with ATMOSPHERIC_MEASUREMENTS table in weather database
	def updateTable(self, message):
  #	insert(list[0],list[1],list[3] 

class SubscriberVisualization(Subscriber):
  # import python graph library
	def __init__(self, name):
	Subscriber.__init__(self, name)
	def graphicallyDisplay(self, message):
  # graph data points

class SubscriberAlexa(Subscriber):
  # technically will subscriber the MQTT broker I presume
	def __init__(self, message):
	Subscriber.__init__(self, message):
	def transferDataToBroker(self, message):
  # send measurements from python to broker
class Publisher:
    def __init__(self,events):
        self.subscribers = dict()
    # helper method used in for loop to send messages
    def get_subscribers(self, event):
        return self.subscribers[event]
	def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscriber[who] = callback
  # map subscriber object to it's particular callback function
    def unregister(self, who):
        del self.subscriber[who]
    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
			callback(message)
            

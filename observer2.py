class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{} got message '{}'".format(self.name,message))
        
class Publisher:
    def __init__(self,events):
        self.subscribers = { event : dict()
                 for event in events }
  # publisher object contains a list of events which map to particular subscriber object(s)
  # flexibile usage of dictionary compression: all subscribers need not recieve the same message as other subscribers
  # useful for alexa interface, map voice commands to either one event, two events, or all events
  # getting one of the three individual measurements (Temperature, Humidity, Pressure) constitute the event types
  
    # helper method used in for loop to send messages
    def get_subscribers(self, event):
        return self.subscribers[event]
    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
from Measurements import Measurement
class Temperature(Measurement):
    def __init__(self, value, units):
        value = value * 9/5 + 32
        units = 'Farhenheit'
        self.__init__(value, units)
        theRange = [-40, 185]
    def getMeasurement(self):
        return self.value
    def getRange(self):
        return self.theRange
 
t = Measurement(85, 'celsius')
print(t.getMeasurement())
        
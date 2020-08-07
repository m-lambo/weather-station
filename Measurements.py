class Measurement:
    def __init__(self, value, units):
        pass
    def getValue(self):
        pass
    def getUnits(self):
        pass
    def getRange(self, bound):
        pass
    
class Humidity(Measurement):
    def __init__(self, value, units, theRange):
        self.value = value
        self.units = units
        self.theRange = theRange  # 0-100%
    def getValue(self):
        return self.value
    def getUnits(self):
        return self.units
    def getRange(self, bound):
        if bound is 'lower':
            return self.theRange[0]
        elif bound is'upper':
            return self.theRange[1]

class Pressure(Measurement):
    def __init__(self, value, units, theRange):
        self.value = value
        self.units = units
        self.theRange = theRange  # 300-1100 hPa
    def getValue(self):
        return self.value
    def getUnits(self):
        return self.units
    def getRange(self, bound):
        if bound is 'lower':
            return self.theRange[0]
        elif bound is 'upper':
            return self.theRange[1]
        
class Temperature(Measurement):
    def __init__(self, value, units, theRange):
        self.value = value * 9/5 + 32
        self.units = 'Farhenheit'
        self.theRange = theRange  # -40-185
    def getValue(self):
        return self.value
    def getUnits(self):
        return self.units
    def getRange(self, bound):
        if bound is 'lower':
            return self.theRange[0]
        elif bound is 'upper':
            return self.theRange[1]
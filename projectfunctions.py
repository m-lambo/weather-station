import time

startSeconds = 0

def startLoop(currentSeconds):
    if currentSeconds == startSeconds:
        return True
    return False
def takeMeasurementNow(currentSeconds):
    if currentSeconds % 10 == 0:
        return True
    return False
def waitOneSec(currentSeconds):
    nextTupleItem = currentSeconds
    while nextTupleItem == currentSeconds:
        timeTicks = time.time()
        timeTuple = time.localtime(timeTicks)
        nextTupleItem = timeTuple[5]
    return nextTupleItem

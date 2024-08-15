import threading
from queue import Queue

class Plane:
    def __init__(self, planeID):
        self.planeID = planeID
        self.currentLocation = "airspace"
        self.ready = False
    
    def advance(self):
        pass

class AirTrafficController:
    def __init__(self):
        self.planes = {}
        self.queues = {
            "airspace" : Queue(),
            "arrival_taxi" : Queue(),
            "gate" : Queue(),
            "departure_taxi" : Queue(),
            "exit" : Queue()
        }
        self.lock = threading.Lock()


from engine import *
from vehicle import *

engine = Engine("V6")
vehicle = Vehicle("Car", True, engine)
vehicle.engine.startEngine() # composition HAS-A
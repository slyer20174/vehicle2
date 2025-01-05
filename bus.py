class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(vehicle):
    pass
school_bus=bus("volvo",670,20)
print(school_bus.name)
print(school_bus.maxspeed)
print(school_bus.mileage)
class Car():
    def __init__(self, **kwargs):
        self.wheel = 4
        self.doors = 4
        self.color = kwargs.get('color', 'red')
        self.price = kwargs.get('price', '10$')
        
class convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 50
    def take_off(self):
        return 'take off'
    def __str__(self):
        return 'dfd dfdfd'
    
conver = convertible()

print(conver.wheel, conver.time, conver.doors)
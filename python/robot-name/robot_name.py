from random import Random
from datetime import datetime

# 65-90 == A-Z

def generate_name():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    generator = Random(timestamp)
    x = chr(generator.randint(65,90))
    y = chr(generator.randint(65,90))
    z = generator.randint(100,999)
    return '{}{}{}'.format(x,y,z)

class Robot:
    
    def __init__(self):
            self.__name = generate_name()

    @property
    def name(self):
        return self.__name

    def reset(self):
        self.__name = generate_name()



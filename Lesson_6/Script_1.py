import time


class TrafficLight:
    __color = ''

    def __init__(self):
        pass

    def running(self, count=1):
        i = 0

        while i < count:
            __color = "red"
            print(__color)
            time.sleep(7)
            __color = "yellow"
            print(__color)
            time.sleep(2)
            __color = "green"
            print(__color)
            time.sleep(7)
            i += 1


light = TrafficLight()
light.running(2)

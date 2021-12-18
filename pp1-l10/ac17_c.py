class Thermometer():
    def __init__(self):
        self.temperature = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temp(self):
        import random
        if self.is_on:
            self.temperature = float("{:.2f}".format(random.uniform(34.0, 42.0)))

    def display(self):
        if self.temperature > 37.0:
            if self.temperature > 41.0:
                print(f"Temperature: {self.temperature}C (fever) CRITICAL TEMPERATURE!")
            else:
                print(f"Temperature: {self.temperature}C (fever)")
        else:
            print(f"Temperature: {self.temperature}C")


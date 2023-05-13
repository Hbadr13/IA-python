import time
from random import randint
import os
# source https://www.youtube.com/watch?v=lHv03rRdRp0


class CoffeeMachine():
    water_level = 100

    def log(function):
        def otherFunction(self, *args, **kwargs):
            before = time.time()
            l = function(self, *args, **kwargs)
            after = time.time()
            delta = after - before
            if os.path.exists("machine.log"):
                file = open("machine.log", 'a')
                file.write(f"(%s) "%os.getenv("USER"))
                file.write("Running: ")
                file.write(str(function.__name__).replace("_"," ").ljust(20,' '))
                if delta < 0.001:
                    file.write(f"[ exec-time = %.3f ms ]"% float(delta*1000))
                else:
                    file.write(f"[ exec-time = %.3f s  ]"% delta)
                file.write("\n")
            return l
        return otherFunction

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    if os.path.exists("machine.log"):
        file = open("machine.log", 'a')
        file.truncate(0)
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

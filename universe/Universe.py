# Universe Simulation
# Trying to simulate the universe, realistically
# License: GNU GPL v3
# (c) 2025 Novixx Systems

from universe.Objects import Gas, Dust
import json

class Universe:
    def __init__(self):
        self.objects = []
        self.time = 0
        self.running = False

    def start(self):
        self.running = True
        # Will add a way for users to select a theory of the universe's creation, for now
        # we will use the Big Bang theory
        self.big_bang()
        while self.running:
            self.update()
            self.time += 1

    def big_bang(self):
        # Create gas objects
        gas1 = Gas((0, 0, 0), 1e10, (1, 0, 0))
        gas2 = Gas((0, 0, 1), 1e10, (0, 1, 0))
        gas3 = Gas((0, 0, 2), 1e10, (0, 0, 1))
        self.objects.extend([gas1, gas2, gas3])

        # Create dust objects
        dust1 = Dust((0, 0, 0), 1e5, (1, 0, 0))
        dust2 = Dust((0, 0, 1), 1e5, (0, 1, 0))
        dust3 = Dust((0, 0, 2), 1e5, (0, 0, 1))
        self.objects.extend([dust1, dust2, dust3])

    def update(self):
        for obj in self.objects:
            print (json.dumps(obj.__dict__))
            obj.update(self.time)

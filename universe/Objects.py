# Universe Simulation
# Trying to simulate the universe, realistically
# License: GNU GPL v3
# (c) 2025 Novixx Systems

global G, c, h

# Helper functions
def calculate_force(mass1, mass2, distance):
    """
    Calculate gravitational force between two masses separated by a distance.
    """
    if distance == 0:
        return 0
    return G * mass1 * mass2 / distance ** 2

def calculate_energy(mass, speed):
    """
    Calculate kinetic energy of an object given its mass and speed.
    """
    return 0.5 * mass * speed ** 2

class Gas:
    """
    Represents a gas object in the universe.
    """
    def __init__(self, position, mass, speed):
        self.position = position  # Position as a tuple (x, y, z)
        self.mass = mass
        self.speed = speed
        self.acceleration = (0, 0, 0)

    def update(self, time):
        """
        Update the gas object's position and speed.
        """
        self.update_position()
        self.update_speed()

    def update_position(self):
        """
        Update the gas object's position.
        """
        self.position = (
            self.position[0] + self.speed[0],
            self.position[1] + self.speed[1],
            self.position[2] + self.speed[2]
        )

    def update_speed(self):
        """
        Update the gas object's speed.
        """
        self.speed = (
            self.speed[0] + self.acceleration[0],
            self.speed[1] + self.acceleration[1],
            self.speed[2] + self.acceleration[2]
        )

class Dust:
    """
    Represents a dust object in the universe.
    """
    def __init__(self, position, mass, speed):
        self.position = position  # Position as a tuple (x, y, z)
        self.mass = mass
        self.speed = speed
        self.acceleration = (0, 0, 0)

    def update(self, time):
        """
        Update the dust object's position and speed.
        """
        self.update_position()
        self.update_speed()

    def update_position(self):
        """
        Update the dust object's position.
        """
        self.position = (
            self.position[0] + self.speed[0],
            self.position[1] + self.speed[1],
            self.position[2] + self.speed[2]
        )

    def update_speed(self):
        """
        Update the dust object's speed.
        """
        self.speed = (
            self.speed[0] + self.acceleration[0],
            self.speed[1] + self.acceleration[1],
            self.speed[2] + self.acceleration[2]
        )

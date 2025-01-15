# Universe Simulation
# Trying to simulate the universe, realistically
# License: GNU GPL v3
# (c) 2025 Novixx Systems

G = 6.67430e-11 # Gravitational constant
c = 299792458 # Speed of light
h = 6.62607015e-34 # Planck constant

from universe.Universe import Universe

def main():
    print ("Universe Simulation - (c) 2025 Novixx Systems")
    universe = Universe()
    universe.start()

if __name__ == "__main__":
    main()

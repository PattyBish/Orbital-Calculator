#!/usr/bin/env python3
"""Orbital period calculator: how long a satellite takes to circle Earth."""
import math

MU = 398600.4418         # Earth's gravitational parameter (km^3/s^2)
EARTH_RADIUS = 6378.137  # km

# Example orbits: (name, altitude in km)
ORBITS = [
    ("ISS (LEO)", 420),
    ("GPS (MEO)", 20200),
    ("Geostationary (GEO)", 35786),
]

def orbital_period(altitude):
    """Return the orbital period in seconds for a circular orbit at this altitude."""
    radius = EARTH_RADIUS + altitude                  # distance from Earth's center
    return 2 * math.pi * math.sqrt(radius**3 / MU)    # Kepler's third law

def orbital_velocity(altitude):
    """Return the orbital speed in km/s for a circular orbit at this altitude."""
    radius = EARTH_RADIUS + altitude
    return math.sqrt(MU / radius)

for name, altitude in ORBITS:
    period = orbital_period(altitude)
    speed = orbital_velocity(altitude)
    print(f"{name}: {altitude} km -> {period / 60:.1f} minutes ({period / 3600:.2f} hours), "
          f"{speed:.2f} km/s")

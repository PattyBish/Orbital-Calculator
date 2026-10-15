#!/usr/bin/env python3
"""Orbital period calculator: how long a satellite takes to circle Earth."""
import math

MU = 398600.4418         # Earth's gravitational parameter (km^3/s^2)
EARTH_RADIUS = 6378.137  # km

altitude = 420  # km above Earth's surface (about where the ISS flies)

radius = EARTH_RADIUS + altitude                     # distance from Earth's center
period = 2 * math.pi * math.sqrt(radius**3 / MU)     # Kepler's third law (seconds)

minutes = period / 60
hours = period / 3600

print(f"Altitude: {altitude} km")
print(f"Orbital period: {minutes:.1f} minutes ({hours:.2f} hours)")

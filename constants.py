import numpy
from math import pi

gravity = -9.8
iterations = 1000
sleep_time = 1/60

max_force = 100

two_pi = numpy.pi * 2

# Back Leg
ampBackLeg = numpy.pi/8
freqBackLeg = 20
phaseOffsetBackLeg = 0
# Front Leg
ampFrontLeg = numpy.pi/4
freqFrontLeg = 20
phaseOffsetFrontLeg = 0
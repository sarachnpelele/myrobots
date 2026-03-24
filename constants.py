import numpy
from math import pi

gravity = -9.8
iterations = 1000
sleep_time = 1/240

max_force = 100

# Back Leg
ampBackLeg = numpy.pi/8
freqBackLeg = 20
phaseOffsetBackLeg = 0
# Front Leg
ampFrontLeg = numpy.pi/4
freqFrontLeg = 20
phaseOffsetFrontLeg = 0

numberOfGenerations = 10

populationSize = 2
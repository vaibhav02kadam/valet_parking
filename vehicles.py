#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math


class Car:
    maxSteerAngle = 0.6
    steerPresion = 10
    wheelBase = 2.8
    axleToFront = 4.5
    axleToBack = 1
    width = 3

    def drawCar(x, y, yaw, color='black'):
        car = np.array([[-Car.axleToBack, -Car.axleToBack, Car.axleToFront, Car.axleToFront, -Car.axleToBack],
                        [Car.width / 2, -Car.width / 2, -Car.width / 2, Car.width / 2, Car.width / 2]])

        rotationZ = np.array([[math.cos(yaw), -math.sin(yaw)],
                        [math.sin(yaw), math.cos(yaw)]])
        car = np.dot(rotationZ, car)
        car += np.array([[x], [y]])
        plt.plot(car[0, :], car[1, :], color)


class TruckTrailer:
    wheelBase = 3.0
    axleWidth = 1.75
    d1 = 5.0

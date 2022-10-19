#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math


class AckermannCar:
    def __init__(self) -> None:
    
        self.maxSteerAngle = 0.6
        self.steerPresion = 10

        self.wheelBase = 2.8 # meters
        self.axleToFront = 4.8 # L + 1
        self.axleToBack = 1 # m 
        self.width = 3.0 # meters

    def drawVehicle(self, x, y, yaw, color='black'):
        car = np.array([[-self.axleToBack, -self.axleToBack, self.axleToFront, self.axleToFront, -self.axleToBack],
                        [self.width / 2, -self.width / 2, -self.width / 2, self.width / 2, self.width / 2]])

        rotationZ = np.array([[math.cos(yaw), -math.sin(yaw)],
                        [math.sin(yaw), math.cos(yaw)]])
        car = np.dot(rotationZ, car)
        car += np.array([[x], [y]])
        plt.plot(car[0, :], car[1, :], color,  linewidth=2.5)


class TruckTrailer:
    wheelBase = 3.0
    axleWidth = 1.75
    d1 = 5.0

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math


class AckermannCar:    
    maxSteerAngle = 0.6
    steerPrecision = 10
    wheelBase = 2.8 # meters
    axleToFront = 4.8 # L + 1
    axleToBack = 1 # m 
    width = 3.0 # meters


def drawCar(x, y, yaw, color='grey'):
    car = np.array([[-AckermannCar.axleToBack, -AckermannCar.axleToBack, AckermannCar.axleToFront, AckermannCar.axleToFront, -AckermannCar.axleToBack],
                    [AckermannCar.width / 2, -AckermannCar.width / 2, -AckermannCar.width / 2, AckermannCar.width / 2, AckermannCar.width / 2]])

    rotationZ = np.array([[math.cos(yaw), -math.sin(yaw)],
                    [math.sin(yaw), math.cos(yaw)]])
    car = np.dot(rotationZ, car)
    car += np.array([[x], [y]])
    plt.plot(car[0, :], car[1, :], color,  linewidth=1)



class TruckTrailer:
    maxSteerAngle = 0.6
    width = 3.0
    wheelBase = 3.0
    axleWidth = 1.75
    d1 = 5.0

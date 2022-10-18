#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
import math

class Car:
    maxSteerAngle = 0.6
    steerPresion = 10
    wheelBase = 3.5
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


class MapEnv:
    def __init__(self,width, height) -> None:
        self.width = width
        self.height = height
        self.envXCoord, self.envYCoord = [], []
        self.left_obs_anchor  = [5, 5]
        self.right_obs_anchor  = [70, 5]
        self.center_obs_anchor = [40, 50]
        self.obs_width = 25
        self.obs_height = 10
        self.obs_delta = 20

    def buildEnv(self):
        
        for row in range(self.height):
            for col in range(self.width):

                #Plotting along X border
                if row == 0:
                    self.envXCoord.append(col)
                    self.envYCoord.append(0)

                #Plotting along Y border
                if col == 0:
                    self.envXCoord.append(0)
                    self.envYCoord.append(row)

                #Plotting along X-Opposite border
                if row == (self.height-1):
                    self.envXCoord.append(col)
                    self.envYCoord.append(self.height-1)

                #Plotting along Y-Opposite border
                if col == (self.width-1):
                    self.envXCoord.append(self.width-1)
                    self.envYCoord.append(row)

                #Plotting left obstacle
                if col >= self.left_obs_anchor[0] and col <= (self.left_obs_anchor[0] + self.obs_width):
                    if row >= self.left_obs_anchor[1] and row <= (self.left_obs_anchor[1] + self.obs_height):
                        self.envXCoord.append(col)
                        self.envYCoord.append(row)

                #Plotting right obstacle
                if col >= self.right_obs_anchor[0] and col <= (self.right_obs_anchor[0] + self.obs_width):
                    if row >= self.right_obs_anchor[1] and row <= (self.right_obs_anchor[1] + self.obs_height):
                        self.envXCoord.append(col)
                        self.envYCoord.append(row)
    
                #Plotting right obstacle
                if col >= self.center_obs_anchor[0] and col <= (self.center_obs_anchor[0] + self.obs_width + self.obs_delta):
                    if row >= self.center_obs_anchor[1] and row <= (self.center_obs_anchor[1] + self.obs_height):
                        self.envXCoord.append(col)
                        self.envYCoord.append(row)
    


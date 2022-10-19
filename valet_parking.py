#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from visualise import MapEnv, Arrow
from vehicles import AckermannCar 
import math

ENV_WIDTH = 41
ENV_HEIGHT = 41
VEHICLE_TYPE = "car"
ARROW_LEN = 3

def main():

    map = MapEnv(ENV_WIDTH, ENV_HEIGHT)
    map.buildEnv()

    if VEHICLE_TYPE=="car":
        vehicle = AckermannCar()

    start_x, start_y, s_theta = 8.0, 35.0, 0.0
    goal_x, goal_y, g_theta = 18.0, 5.0, 0.0
  
    plt.cla()
    plt.xlim(min(map.envXCoord), max(map.envXCoord)) 
    plt.ylim(min(map.envYCoord), max(map.envYCoord))
    vehicle.drawVehicle(20, 25, 45)

    vehicle.drawVehicle(start_x, start_y, s_theta, 'green')
    vehicle.drawVehicle(goal_x, goal_y, g_theta, 'red')

    plt.arrow(start_x,start_y,  ARROW_LEN*math.cos(s_theta),  ARROW_LEN*math.sin(s_theta), width=.1)

    plt.plot(map.envXCoord, map.envYCoord, "sk")
    plt.plot(ENV_WIDTH, ENV_HEIGHT, linewidth=1.5, color='r', zorder=0)
    plt.axis('equal')

    plt.title("Valet Parking")
    plt.pause(0.001)
    
    plt.show()

if __name__ == '__main__':
    main()
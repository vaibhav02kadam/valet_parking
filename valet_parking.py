#!/usr/bin/env python3

import numpy as np
import math

import matplotlib.pyplot as plt

from visualise import MapEnv, Arrow
import vehicles
from hybrid_astar import*

ENV_WIDTH = 41
ENV_HEIGHT = 41
VEHICLE_TYPE = "car"
ARROW_LEN = 3

def planAckermann():
    map = MapEnv(ENV_WIDTH, ENV_HEIGHT)
    map.buildEnv()

    start_pose = [3.0, 35.0, np.deg2rad(0)]
    goal_pose = [20.0, 5.0, np.deg2rad(0)]

    # Calculating parameters for Ackermann Steering
    map_env = calculateEnvParameters(map.envXCoord, map.envYCoord, 4, np.deg2rad(15.0))
    x, y, yaw = hybridAstar(start_pose, goal_pose, map_env, plt)

    for k in range(len(x)):
        # plt.cla()
        plt.xlim(min(map.envXCoord), max(map.envXCoord)) 
        plt.ylim(min(map.envYCoord), max(map.envYCoord))
        
        vehicles.drawCar(start_pose[0], start_pose[1], start_pose[2], 'green')
        vehicles.drawCar(goal_pose[0], goal_pose[1], goal_pose[2], 'red')

        vehicles.drawCar(x[k], y[k], yaw[k])
        plt.arrow(x[k],y[k],  ARROW_LEN*math.cos(yaw[k]),  ARROW_LEN*math.sin(yaw[k]), width=0.05)

        plt.plot(map.envXCoord, map.envYCoord, "sk")
        plt.plot(x, y, linewidth=1.5, color='r', zorder=1)
        plt.axis('equal')

        plt.title("Valet Parking")
        plt.pause(0.1)
        
    plt.show()

def planTruckTrailer():

    # x , y, theta, theta1
    start_pose = [3.0, 35.0, np.deg2rad(0), np.deg2rad(0)]
    goal_pose = [20.0, 5.0, np.deg2rad(0), np.deg2rad(0)]


def main():

    

    if VEHICLE_TYPE=="car":
         planAckermann()
    
    if VEHICLE_TYPE=="trucktrailer":
        planTruckTrailer()
        

if __name__ == '__main__':
    main()
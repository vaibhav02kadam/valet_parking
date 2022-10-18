#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt

from visualise import MapEnv 

ENV_WIDTH = 101
ENV_HEIGHT = 61


def main():

    map = MapEnv(ENV_WIDTH, ENV_HEIGHT)

    map.buildEnv()
  
    plt.cla()
    plt.xlim(min(map.envXCoord), max(map.envXCoord)) 
    plt.ylim(min(map.envYCoord), max(map.envYCoord))


    plt.plot(map.envXCoord, map.envYCoord, "sk")
    plt.plot(ENV_WIDTH, ENV_HEIGHT, linewidth=1.5, color='r', zorder=0)


    plt.title("Valet Parking")
    plt.pause(0.001)
    
    plt.show()

if __name__ == '__main__':
    main()
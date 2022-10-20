#!/usr/bin/env python3

import numpy as np
import math

import scipy.spatial.kdtree as kd
import matplotlib.pyplot as plt

import CurvesGenerator.reeds_shepp as rs
from vehicles import AckermannCar 


class State:
    def __init__(self, states, trajectory_rollout, steering_angle, traversal_dir, cost, parent_index):
        self.states = states
        self.trajectory_rollout = trajectory_rollout
        self.steering_angle = steering_angle
        self.traversal_dir = traversal_dir
        self.cost = cost
        self.parent_index = parent_index


class getEnvParameters:
    def __init__(self, env_xmin, env_ymin, env_xmax,
     env_ymax, cordinate_resolution, theta_resolution, obstacle_kdtree, obs_x, obs_y):
        self.env_xmin = env_xmin
        self.env_ymin = env_ymin
        self.env_xmax = env_xmax
        self.env_ymax = env_ymax
        self.cordinate_resolution = cordinate_resolution
        self.theta_resolution = theta_resolution
        self.obstacle_kdtree = obstacle_kdtree
        self.obs_x = obs_x
        self.obs_y = obs_y




def motionCommands():
    pass



def kinematicSimulationNode(currentNode, motionCommand, mapParameters, simulationLength=4, step = 0.8 ):
    pass



def reedsSheppNode(currentNode, goalNode, mapParameters):
    pass


def collision(traj, mapParameters):
    pass


def hybridAstar(start_pose, goal_pose, env_map ):
    pass
    #start pose
    #goal pose





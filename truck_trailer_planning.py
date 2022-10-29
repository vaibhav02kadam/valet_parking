#!/usr/bin/env python3


import numpy as np
import math
import heapq

import scipy.spatial.kdtree as kd
import matplotlib.pyplot as plt
from heapdict import heapdict

import CurvesGenerator.reeds_shepp as rs
from vehicles import TruckTrailer

from hybrid_astar import*

# class State:
#     def __init__(self, state_id, trajectory_rollout, steering_angle, traversal_dir, cost, parent_index):
#         self.state_id = state_id
#         self.trajectory_rollout = trajectory_rollout
#         self.steering_angle = steering_angle
#         self.traversal_dir = traversal_dir
#         self.cost = cost
#         self.parent_index = parent_index


# class Cost:
#     reverse = 10
#     direction_change = 150
#     steer_angle = 1
#     steer_angle_change = 5
#     hybrid_cost = 50
#     jack_knife_cost = 200.0


# class getEnvParameters:
#     def __init__(self, env_xmin, env_ymin, env_xmax,
#      env_ymax, cordinate_resolution, theta_resolution, obstacle_kdtree, obs_x, obs_y):
#         self.env_xmin = env_xmin
#         self.env_ymin = env_ymin
#         self.env_xmax = env_xmax
#         self.env_ymax = env_ymax

#         self.cordinate_resolution = cordinate_resolution
#         self.theta_resolution = theta_resolution

#         self.obstacle_kdtree = obstacle_kdtree
#         self.obs_x = obs_x
#         self.obs_y = obs_y


# def calculateEnvParameters(obs_x, obs_y, cordinate_resolution, theta_resolution):
#     env_xmin = round(min(obs_x) / cordinate_resolution)
#     env_ymin = round(min(obs_y) / cordinate_resolution)
#     env_xmax = round(min(obs_x) / cordinate_resolution)
#     env_ymax = round(min(obs_y) / cordinate_resolution)

#     obstacle_kdtree = kd.KDTree([[x, y] for x, y in zip(obs_x, obs_y)])

#     return getEnvParameters(env_xmin, env_ymin, env_xmax, env_ymax,cordinate_resolution,  theta_resolution, obstacle_kdtree, obs_x, obs_y)  


# def getMotionPrimitives():

#     direction = 1 #Forward direction
#     motion_primitives = []

#     for primitive in np.arange(TruckTrailer.maxSteerAngle, -(TruckTrailer.maxSteerAngle/TruckTrailer.steerPrecision), -AckermannCar.maxSteerAngle/AckermannCar.steerPrecision):
#         motion_primitives.append([primitive, direction])
#         motion_primitives.append([primitive, -direction])
#     return motion_primitives






def hybridAstar(start_pose, goal_pose, env_map, plt):

    start_pose_id = [round(start_pose[0] / env_map.cordinate_resolution), \
                round(start_pose[1] / env_map.cordinate_resolution), \
                round(start_pose[2]/env_map.theta_resolution)]

    goal_pose_id = [round(goal_pose[0] / env_map.cordinate_resolution), \
                round(goal_pose[1] / env_map.cordinate_resolution), \
                round(goal_pose[2]/env_map.theta_resolution)]

    motion_primitives = getMotionPrimitives()

    start_state = State(start_pose_id, [start_pose], 0, 1, 0, tuple(start_pose_id))
    goal_state = State(goal_pose_id, [goal_pose], 0, 1, 0, tuple(goal_pose_id))

    unconstrained_heuristics = getUnconstrainedHeuristic(goal_state, env_map)

    open_set = {index(start_state):start_state}
    closed_set = {}

    cost_priority_queue = heapdict()

    cost_priority_queue[index(start_state)] = max(start_state.cost, Cost.hybrid_cost * unconstrained_heuristics[start_state.state_id[0]][start_state.state_id[1]])

    counter = 0

    while True:
        counter += 1

        if not open_set:
            return None

        current_state_id = cost_priority_queue.popitem()[0]
        current_state = open_set[current_state_id]


        rs_node = reeds_shepp_node(current_state, goal_state, env_map)

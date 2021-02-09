#!/bin/bash
colcon build
source ./install/setup.bash
export GAZEBO_MODEL_PATH=./src/myrobot/models/
rviz2 -d src/myrobot/resource/myrobot2.rviz & ros2 launch myrobot turtlebot3_world.launch.py

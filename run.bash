#!/bin/bash
rm -rf /build /install /log
colcon build
source ./install/setup.bash
export GAZEBO_MODEL_PATH=./src/myrobot/models/
# export ROS_PACKAGE_PATH=./src/
rviz2 -d src/myrobot/resource/myrobot3.rviz & ros2 launch myrobot turtlebot3_world.launch.py

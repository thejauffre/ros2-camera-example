#!/bin/bash
colcon build
source ./install/setup.bash
export GAZEBO_MODEL_PATH=./src/myrobot/models/


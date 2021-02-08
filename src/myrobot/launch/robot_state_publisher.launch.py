#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Darby Lim

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

package_name = 'myrobot'


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'structure.urdf'

    print('urdf_file_name : {}'.format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory(package_name),
        'models',
        urdf_file_name)

    x = '0'
    y ='0'
    z ='0'
    roll ='0'
    pitch = '0'
    yaw ='0'
    link_1 = 'link'
    base_scan1 = 'base_scan1'
    base_scan2 = 'base_scan2'

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            node_executable='robot_state_publisher',
            node_name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            node_name='static_transform_publisher',
            output='screen',
            arguments=[x, y, z, yaw, pitch, roll, link_1, base_scan1],
        ),

        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            node_name='static_transform_publisher',
            output='screen',
            arguments=[x, y, z, yaw, pitch, roll, link_1, base_scan2],
        )
    ])

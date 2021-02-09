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
    urdf_file_name = 'forklift.urdf'

    print('urdf_file_name : {}'.format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory(package_name),
        'models',
        urdf_file_name)
    
    link_main = 'main_base'
    link_chassis = 'forklift_chassis'
    link_right = 'right_wheel'
    link_left = 'left_wheel'
    link_back = 'back_wheel'

    x_0 = '0'
    y_0 ='0'
    z_0 ='0'
    roll_0 ='0'
    pitch_0 = '0'
    yaw_0 ='0'

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            namespace="forklift",
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='forklift_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

## Static links transforms
        Node(
            namespace="forklift",
            package='tf2_ros',
            executable='static_transform_publisher',
            name='forklift_static_transform_publisher',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, link_chassis, link_main],
        ),
        Node(
            namespace="forklift",
            package='tf2_ros',
            executable='static_transform_publisher',
            name='forklift_static_transform_publisher',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, link_right, link_chassis],
        ),
        Node(
            namespace="forklift",
            package='tf2_ros',
            executable='static_transform_publisher',
            name='forklift_static_transform_publisher',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, link_left, link_chassis],
        ),
        Node(
            namespace="forklift",
            package='tf2_ros',
            executable='static_transform_publisher',
            name='forklift_static_transform_publisher',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, link_back, link_chassis],
        ),
    ])

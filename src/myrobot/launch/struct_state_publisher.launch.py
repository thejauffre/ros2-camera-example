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
namespace = 'structure'

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    urdf_file_name = 'structure.urdf'

    print('urdf_file_name : {}'.format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory(package_name),
        'models',
        urdf_file_name)
    
    link_main = 'main_base'
    x_1 = '0'
    y_1 ='-1.9'
    z_1 ='2.9'
    roll_1 ='0'
    pitch_1 = '1.57'
    yaw_1 ='0'
    base_scan1 = 'base_scan1'

    x_2 = '0'
    y_2 ='1.9'
    z_2 ='2.9'
    roll_2 ='0'
    pitch_2 = '1.57'
    yaw_2 ='3.14'
    base_scan2 = 'base_scan2'

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
            #namespace = namespace,
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

## Laser data transforms
        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            arguments=[x_1, y_1, z_1, yaw_1, pitch_1, roll_1, link_main, base_scan1],
        ),

        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            output='screen',
            arguments=[x_2, y_2, z_2, yaw_2, pitch_2, roll_2, link_main, base_scan2],
        ),

## Static links transforms
        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher1',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, 'laser1_link', link_main],
        ),
        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher2',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, 'laser2_link', link_main],
        ),
        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher3',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, 'side_one', link_main],
        ),
        Node(
            #namespace = namespace,
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher4',
            output='screen',
            arguments=[x_0, y_0, z_0, yaw_0, pitch_0, roll_0, 'side_two', link_main],
        ),

    ])

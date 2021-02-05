from setuptools import setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
from ament_index_python.packages import get_package_share_directory

package_name = 'myrobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('models/*')),
        (os.path.join('share', package_name, 'urdfs'), glob('urdfs/*.*')),
        (os.path.join('share', package_name, 'sdfs'), glob('sdfs/*.*')),
        (os.path.join('share', package_name, 'sdfs', 'turtlebot3_burger'), glob('sdfs/turtlebot3_burger/*.*')),
        (os.path.join('share', package_name, 'sdfs', 'turtlebot3_burger','meshes'), glob('sdfs/turtlebot3_burger/meshes/*.*')),
        (os.path.join('share', package_name, 'sdfs', 'turtlebot3_world'), glob('sdfs/turtlebot3_world/*.*')),
        (os.path.join('share', package_name, 'sdfs', 'turtlebot3_world','meshes'), glob('sdfs/turtlebot3_world/meshes/*.*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.*')),
        (os.path.join('share', package_name, 'meshes', 'bases'), glob('meshes/bases/*.*')),
        (os.path.join('share', package_name, 'meshes', 'sensors'), glob('meshes/sensors/*.*')),
        (os.path.join('share', package_name, 'meshes', 'wheels'), glob('meshes/wheels/*.*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andrea',
    maintainer_email='thejauffre@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'state_publisher = myrobot.state_publisher:main'
        ],
    },
)

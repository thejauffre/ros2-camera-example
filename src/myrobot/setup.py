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
        (os.path.join('share', package_name, 'models'), glob('models/*.*')),
        (os.path.join('share', package_name, 'models', 'turtlebot3_burger'), glob('models/turtlebot3_burger/*.*')),
        (os.path.join('share', package_name, 'models', 'turtlebot3_burger','meshes'), glob('models/turtlebot3_burger/meshes/*.*')),
        (os.path.join('share', package_name, 'models', 'turtlebot3_world'), glob('models/turtlebot3_world/*.*')),
        (os.path.join('share', package_name, 'models', 'turtlebot3_world','meshes'), glob('models/turtlebot3_world/meshes/*.*')),
        (os.path.join('share', package_name, 'models', 'meshes'), glob('models/meshes/*.*')),
        (os.path.join('share', package_name, 'models', 'meshes', 'bases'), glob('models/meshes/bases/*.*')),
        (os.path.join('share', package_name, 'models', 'meshes', 'sensors'), glob('models/meshes/sensors/*.*')),
        (os.path.join('share', package_name, 'models', 'meshes', 'wheels'), glob('models/meshes/wheels/*.*')),

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
            'state_publisher = myrobot.state_publisher:main'
        ],
    },
)

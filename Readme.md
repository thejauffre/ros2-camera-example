# ROS2 workspace example
## Description
This is a sample ROS2 workspace, with a package and two main dependencies:  
1. **v4l2_camera**: camera publisher (*/image_raw*) - [follow this guide](https://index.ros.org/r/v4l2_camera/)  
Install using *sudo apt install ros-foxy-v4l2-camera*  
2. **vision_opencv**: set of tools with cv_bridge to convert image_raw data to opencv (and other things) - [follow this guide](https://index.ros.org/p/cv_bridge/github-ros-perception-vision_opencv/)  
Install using *sudo apt install ros-foxy-vision-opencv*
3. **mypkg**: simple image subscriber/publisher created following [this guide](https://index.ros.org/doc/ros2/Tutorials/Creating-Your-First-ROS2-Package/)

## Sequence to create a new package

Typical workspace folder structure:
```
workspace_folder/
    src/
      package_1/
          CMakeLists.txt
          package.xml

      package_2/
          setup.py
          package.xml
          resource/package_2
      ...
      package_n/
          CMakeLists.txt
          package.xml
```

First, create a package with *ros2 pkg create --build-type ament_cmake <package_name>* (or ament_python).

Then, customize *package.xml* with info about license, developer, name...

Create your publisher/listener inside workspace/src/mypkg/mypkg folders (i.e. create a *mypkg_function.py* script).

If using python, edit setup.py adding the correct entrypoints:
```
entry_points={
        'console_scripts': [
                'talker = mypkg.mypkg_function:second',
                'listener = mypkg.mypkg_function:main',
        ],
},
```
Build using colcon, then launch.

**Note**: you can also use *cmake* to properly setup a package before building it; i.e. specifying a compiler (c++/g++/gcc) and install directories.

## Useful commands
First you have to source the ROS2 environment (your script is in */scripts/ros2_launch.sh*).  
**Display active nodes**: *rqt_graph* ;   
**Build a package (or all)** *colcon build --packages-select mypkg* (or *colcon build*) ;  
**Remember: source installed packages**: *source install/local_setup.bash* from within the workspace;  
**Launch your custom node**: *ros2 run mypkg listener* ;  
**Launch via multicast**: *ROS_DOMAIN_ID=13 ros2 run mypkg publisher* ;


## Additional notes  
**Original forklift model**: [downloaded from here](https://open3dmodel.com/3d-models/forklift_476994.html/)  


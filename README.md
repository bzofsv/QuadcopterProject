# QuadcopterProject

Code and updates for my quadcopter project using a D435i to identify, track, and follow targets. 

Built on Ubuntu 20.04.6
Install ROS Noetic first

ORB SLAM2 for D435i camera is in the ORB_SLAM2 folder, corrected for Pangolin 0.8, Eigen 3.4.0, C++14, and ROS Noetic packaged OpenCV 4.2.0

Install dependencies, Eigen 3.4.0 and Pangolin 0.8 first, then run build.sh and build_ros.sh in the ORB SLAM folder to build ORB SLAM. With ROS installed, OpenCV does not need to be seperately installed.

This version of ROS ORB SLAM reads from /camera/color/image_raw and /camera/depth/image_rect_raw instead of the default /camera/rgb/image_raw and /camera/depth_registered/image_raw


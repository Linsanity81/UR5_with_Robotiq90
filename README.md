# UR5_with_Robotiq90
ur5
===

ROS packages for the UR5 Robot with a Robotiq90 gripper. We use robotiq85 to immitate the real Robotiq90 gripper.



## Visualization of UR5 in RViz

To visualize the model of the robot with a gripper, launch the following:
  ```
  $ roslaunch ur5_with_robotiq90_config demo.launch
  ```
  
## Control real UR5 by the keyboard input

To control real UR5, launch the following:
  ```
  $ roslaunch ur5_with_robotiq90_config ur5_bringup.launch robot_ip:=IP_OF_YOUR_ROBOT
  $ rosrun ur5_with_robotiq90_config demo.py
  ```
You can control the arm by keyboard now.


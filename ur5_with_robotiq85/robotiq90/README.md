# robotiq90

ROS metapackage developed by the [NEO GROUP] from the [ShanTou University, China]. 

This package is modified from the robotiq package developed by the [Control Robotics Intelligence Group](http://www.ntu.edu.sg/home/cuong/) from the [Nanyang Technological University, Singapore](http://www.ntu.edu.sg).

## Maintainer

[Rulin Chen](https://github.com/Linsanity81)

## Setup

  * Robotiq 90 Gripper with simple Controller. (Modbus TCP/IP)


## Documentation

  * See the installation instructions below.
  * Throughout the various files in this repository.

### Testing the Installation

Be sure to always source the appropriate ROS setup file, e.g:
```{bash}
source ~/catkin_ws/devel/setup.bash
```
You might want to add that line to your `~/.bashrc`

Try the `cmodel_simple_controller`:
```{bash}
roslaunch robotiq_control cmodel_simple_controller.launch ip:=ROBOTIQ_IP_ADDRESS
```
Expected output:
```
Simple C-Model Controller
-----
Current command:  rACT = 0, rGTO = 0, rATR = 0, rPR = 0, rSP = 0, rFR = 0 (Perhap different)
-----
Available commands

r: Reset
c: Close
o: Open
(0-4095): Go to that position
f: Faster
l: Slower
i: Increase force
d: Decrease force
-->
```

#!/usr/bin/env python
import rospy
from robotiq_msgs.msg import Command
from time import sleep

def genCommand(char, command):
  """Update the command according to the character entered by the user."""    
  if char == 'o':
    command = Command();
    command.SAFE_MODE = 0
    command.MEASURE = 1
    command.MEASURE_INPUT = 1
    command.POSITION  = 4095
    command.VELOCITY  = 400
    command.FORCE  = 200

  if char == 'r':
    command = Command();
    command.SAFE_MODE = 0
    command.MEASURE = 1
    command.MEASURE_INPUT = 1
    command.POSITION  = 2000
    command.VELOCITY  = 400
    command.FORCE  = 200

  if char == 'c':
    command = Command();
    command.SAFE_MODE = 0
    command.MEASURE = 1
    command.MEASURE_INPUT = 1
    command.POSITION  = 3300
    command.VELOCITY  = 400
    command.FORCE  = 200

  #If the command entered is a int, assign this value to rPRA
  try: 
    command.POSITION = int(char)
    if command.POSITION > 4095:
      command.POSITION = 4095
    if command.POSITION < 0:
      command.POSITION = 0
  except ValueError:
    pass

  if char == 'f':
    command.VELOCITY += 25
    if command.VELOCITY > 1000:
      command.VELOCITY = 1000

  if char == 'l':
    command.VELOCITY -= 25
    if command.VELOCITY < 0:
      command.VELOCITY = 0

  if char == 'i':
    command.FORCE += 25
    if command.FORCE > 1000:
      command.FORCE = 1000

  if char == 'd':
    command.FORCE -= 25
    if command.FORCE < 0:
      command.FORCE = 0
  return command

def askForCommand(command):
  """
  Ask the user for a command to send to the gripper.
  """
  currentCommand  = 'Simple C-Model Controller\n-----\nCurrent command:'
  currentCommand += '  SAFETY_MODE = '  + str(command.SAFE_MODE)
  currentCommand += ', MEASURE = '  + str(command.MEASURE)
  currentCommand += ', MEASURE_INPUT = '  + str(command.MEASURE_INPUT)
  currentCommand += ', POSITION = '   + str(command.POSITION )
  currentCommand += ', VELOCITY = '   + str(command.VELOCITY )
  currentCommand += ', FORCE = '   + str(command.FORCE )
  print currentCommand
  strAskForCommand  = '-----\nAvailable commands\n\n'
  strAskForCommand += 'r: Reset\n'
  strAskForCommand += 'c: Close\n'
  strAskForCommand += 'o: Open\n'
  strAskForCommand += '(0-4095): Go to that position\n'
  strAskForCommand += 'f: Faster\n'
  strAskForCommand += 'l: Slower\n'
  strAskForCommand += 'i: Increase force\n'
  strAskForCommand += 'd: Decrease force\n'
  strAskForCommand += '-->'
  return raw_input(strAskForCommand)

def publisher():
  """
  Main loop which requests new commands and publish them on the CModelRobotOutput topic.
  """
  rospy.init_node('robotiq_simple_controller')
  pub = rospy.Publisher('command', Command, queue_size=3)
  command = Command()
  while not rospy.is_shutdown():
    command = genCommand(askForCommand(command), command)
    pub.publish(command)
    rospy.sleep(0.1)

if __name__ == '__main__':
  publisher()

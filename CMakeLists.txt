cmake_minimum_required(VERSION 2.8.3)
project(xbox_controller)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  message_generation
)

add_service_files(
  FILES
  Rumble.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

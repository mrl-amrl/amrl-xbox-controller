## Rumble Effect for Xbox360

#### Installation

```
$ cd catkin_ws/src
$ git clone https://github.com/mrl-amrl/xbox-controller
$ cd catkin_ws
$ catkin_make
```

#### Usage

**Note** Make sure your `/dev/input/eventX` has permission to access. You can do it with `udev` or `chmod`.

List of devices available in your system:

```
$ rosrun xbox_controller get_devices
```

ROS node with service handler:

```
$ rosrun xbox_controller controller
```

You can also set `device` parameter in your launch file. If `device` parameter not exists in your ROS parameters, controller node will scan your devices and choose one of your Xbox events as default parameter.

```
$ rosservice call /xbox_controller/rumble "duration: 500"
```

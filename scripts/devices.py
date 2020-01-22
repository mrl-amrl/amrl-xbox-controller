def get_devices():
    device_lines = []
    with open('/proc/bus/input/devices', 'r') as handler:
        device_lines = handler.readlines()

    name = ""
    handlers = []
    devices = {}
    for i, device_line in enumerate(device_lines):
        device_line = str(device_line[:-1])

        if device_line.startswith("I:") or i == len(device_lines) - 1:
            if name != "":
                devices[name] = handlers
        else:
            if device_line.startswith('N:'):
                name = device_line[9:-1]
            if device_line.startswith('H:'):
                handlers = device_line[12:-1].split(" ")
    return devices

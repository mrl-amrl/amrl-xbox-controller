import time
from evdev import ecodes, ff, InputDevice

class Effect:
    def __init__(self, device, duration_ms):
        rumble = ff.Rumble(strong_magnitude=0xc000, weak_magnitude=0xc000)

        self.effect = ff.Effect(
            ecodes.FF_RUMBLE,  # type
            -1,  # id (set by ioctl)
            0,  # direction
            ff.Trigger(0, 0),  # no triggers
            ff.Replay(duration_ms, 0),  # length and delay
            ff.EffectType(ff_rumble_effect=rumble)
        )
        self.device = device

        self.effect_id = self.device.upload_effect(self.effect)
        self.device.write(ecodes.EV_FF, self.effect_id, 1)
    
    def clean(self):
        self.device.erase_effect(self.effect_id)

class RumbleController:
    def __init__(self, device_path):
        self.device = InputDevice(device_path)

    def do(self, duration_ms):
        effect = Effect(device=self.device, duration_ms=duration_ms)
        time.sleep(duration_ms / 1000.0)
        effect.clean()
    
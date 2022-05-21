# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Media', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000000, '', []),
        (0x000000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, 'Mute Mic', [Keycode.CONTROL, Keycode.SHIFT, 'a']),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, 'Mute Spk', [[ConsumerControlCode.MUTE]]),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x000000, '>||', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x000000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l'])
    ]
}

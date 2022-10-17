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



app = {                 # REQUIRED dict, must be named 'app'
    'name' : 'Control', # Application name
    'macros' : [        # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        ('<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        ('>||', [[ConsumerControlCode.PLAY_PAUSE]]),
        ('>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # 2nd row ----------
        ('', []),
        ('Mute Mic', [Keycode.CONTROL, Keycode.ALT, Keycode.KEYPAD_ONE ]),
        ('', []),
        # 3rd row ----------
        ('Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        ('Mute Spk', [[ConsumerControlCode.MUTE]]),
        ('Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 4th row ----------
        ('[]', [Keycode.WINDOWS, Keycode.TAB]),
        ('Seach', [Keycode.CONTROL, Keycode.ALT, Keycode.KEYPAD_ZERO ]),
        ('Clip', [Keycode.CONTROL, Keycode.ALT, Keycode.KEYPAD_TWO ]),
        # Encoder button ---
        ('', [Keycode.WINDOWS, Keycode.L])
    ]
}

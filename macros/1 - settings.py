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
    'name' : 'Settings', # Application name
    'macros' : [      # List of button macros...
        # LABEL    KEY SEQUENCE
        # 1st row ----------
        ('', []),
        ('', []),
        ('', []),
        # 2nd row ----------
        ('Speed -', ['SPEED-']),
        ('', []),
        ('Speed +', ['SPEED+']),
        # 3rd row ----------
        ('', []),
        ('', []),
        ('', []),
        # 4th row ----------
        ('Brt -', ['BRIGHTNESS-']),
        ('Toggle', ['TOGGLE_RGB']),
        ('Brt +', ['BRIGHTNESS+']),
        # Encoder button ---
        ('', [Keycode.WINDOWS, 'l'])
    ]
}

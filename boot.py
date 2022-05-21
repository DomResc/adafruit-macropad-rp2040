import board
import digitalio
import storage
import usb_cdc

b1 = digitalio.DigitalInOut(board.KEY1)
b1.switch_to_input(pull=digitalio.Pull.UP)

if not b1.value:
    print("dev mode!")
else:
    usb_cdc.disable()
    storage.disable_usb_drive()
# pip install gpiozero

from gpiozero import OutputDevice

class Relay(OutputDevice):
    # TODO: add initializing (done)
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)


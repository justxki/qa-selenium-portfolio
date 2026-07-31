class Toggle:
    def __init__(self):
        self._state = False

    @property
    def state(self):
        return self._state

    def flip(self):
        if not self._state:
            self._state = True
        else:
            self._state = False

    def turn_on(self):
        if self._state:
            raise ValueError("Toggle is already on.")
        else:
            self._state = True

    def turn_off(self):
        if not self._state:
            raise ValueError("Toggle is already off.")
        else:
            self._state = False

#tog = Toggle()
#print(tog.state)
#tog.flip()
#tog.turn_on()
#print(tog.state)
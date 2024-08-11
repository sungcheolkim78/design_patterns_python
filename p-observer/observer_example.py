from observer_base import Observer, Subject


class ClockTimer(Subject):
    def __init__(self):
        super().__init__()
        self._hour = 1
        self._minute = 0
        self._second = 0

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    def tick(self):
        self._second += 1
        if self._second > 59:
            self._minute += 1
            self._second = 0
        if self._minute > 59:
            self._hour += 1
            self._minute = 0
        if self._hour > 12:
            self._hour = 1

        self.notify()


class DigitalClock(Observer):
    def __init__(self, s: ClockTimer):
        self._subject = s
        self._subject.attach(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._subject.detach(self)

    def update(self, the_changed_subject):
        if the_changed_subject == self._subject:
            self.draw()

    def draw(self):
        hour = self._subject.hour
        minute = self._subject.minute
        second = self._subject.second
        if hour > 12:
            hour -= 12
            ampm = "PM"
        else:
            ampm = "AM"

        print(f"Digital {hour:02d}:{minute:02d}:{second:02d} {ampm}")


class AnalogClock(Observer):
    def __init__(self, s: ClockTimer):
        self._subject = s
        self._subject.attach(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._subject.detach(self)

    def update(self, the_changed_subject):
        if the_changed_subject == self._subject:
            self.draw()

    def draw(self):
        hour = self._subject.hour
        minute = self._subject.minute
        second = self._subject.second

        print(f"Analog {hour} hour {minute} minutes {second} seconds")


if __name__ == "__main__":
    timer = ClockTimer()

    with DigitalClock(timer) as digital_clock:
        with AnalogClock(timer) as analog_clock1:
            with AnalogClock(timer) as analog_clock2:
                for i in range(5):
                    timer.tick()

            for i in range(5):
                timer.tick()

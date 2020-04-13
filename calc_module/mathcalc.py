class MathCalc:
    @property
    def first(self):
        return getattr(self, '_first')

    @first.setter
    def first(self, value):
        self._first = int(value)

    @property
    def second(self):
        return getattr(self, '_second')

    @second.setter
    def second(self, value):
        self._second = int(value)

    def add(self):
        return self._first + self._second
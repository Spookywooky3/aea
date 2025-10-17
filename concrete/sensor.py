from __future__ import annotations

from observer import Observer
from subject import Subject


class Sensor(Subject[float]):
    def __init__(self, observer: Observer) -> None:
        super().__init__(observer)
        print(f'Initializing sensor: {id(self)}')

    @property
    def state(self) -> float:
        return self._state

    @state.setter
    def state(self, value: float) -> None:
        self._state = value
        self.notify()

    def notify(self) -> None:
        self._observer.update(self, self.state)

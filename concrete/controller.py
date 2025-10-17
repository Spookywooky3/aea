from __future__ import annotations

from observer import Observer
from subject import Subject
from event import Event

from concrete.sensor import Sensor


class Controller(Observer):
    def __init__(self) -> None:
        super().__init__()

    def configure(self) -> None:
        x = Sensor(self)
        x.state = 32.0

    def update[T](self, subject: Subject[T], event: Event, state: T) -> None:
        match event:
            case Event.STATE_CHANGED:
                print(f"[{id(subject)}] Received state update, new state: {state}")

            case Event.REQUEST_UPDATE:
                print(f'[{id(subject)}] State update requested.')

            case __:
                pass

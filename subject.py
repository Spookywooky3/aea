from __future__ import annotations
from abc import ABC, abstractmethod

from observer import Observer
from event import Event


class Subject[T](ABC):
    @abstractmethod
    def __init__(self, observer: Observer) -> None:
        self._state: T
        self._observer = observer

    @property
    @abstractmethod
    def state(self) -> T:
        """Returns the current state of the subject."""
        pass

    @state.setter
    @abstractmethod
    def state(self, value: T) -> None:
        """Set the state of the subject, must call notify in concrete implementation."""
        pass

    @abstractmethod
    def notify(self, event: Event) -> None:
        """Notify all subscribed observers."""
        pass

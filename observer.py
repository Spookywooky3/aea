from __future__ import annotations
from abc import ABC, abstractmethod

from subject import Subject
from event import Event


class Observer(ABC):
    def __init__(self) -> None:
        self.configure()

    @abstractmethod
    def configure(self) -> None:
        """Instantiate subjects etc."""
        pass

    @abstractmethod
    def update[T](self, subject: Subject[T], event: Event, state: T) -> None:
        """Handle updates from subjects."""
        pass

#!/usr/bin/python3
"""This module defines a LockedClass."""


class LockedClass:
    """Defines a class that restricts the creation of instance attributes."""

    def __setattr__(self, name, value):
        """Customized attribute assignment behavior."""
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")


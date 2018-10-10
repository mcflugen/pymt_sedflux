#! /usr/bin/env python

from .bmi import Sedflux3D, Avulsion, Plume, Subside

__all__ = ["Sedflux3D", "Avulsion", "Plume", "Subside"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

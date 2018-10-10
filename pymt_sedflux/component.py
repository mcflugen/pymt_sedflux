from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Avulsion, Plume, Sedflux3D, Subside

Sedflux3D = bmi_factory(Sedflux3D)
Avulsion = bmi_factory(Avulsion)
Plume = bmi_factory(Plume)
Subside = bmi_factory(Subside)

del bmi_factory

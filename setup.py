#! /usr/bin/env python
import os
import sys

import numpy as np
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension

try:
    import model_metadata
except ImportError:

    def get_cmdclass(*args, **kwds):
        return kwds.get("cmdclass", None)

    def get_entry_points(*args):
        return None


else:
    from model_metadata.utils import get_cmdclass, get_entry_points


import numpy as np


include_dirs = [np.get_include(), os.path.join(sys.prefix, "include")]


libraries = ["bmi_sedflux3d", "bmi_avulsion", "bmi_plume", "bmi_subside"]


library_dirs = []


define_macros = []

undef_macros = []


extra_compile_args = []


ext_modules = [
    Extension(
        "pymt_sedflux.lib._bmi",
        ["pymt_sedflux/lib/_bmi.pyx"],
        language="c",
        include_dirs=include_dirs,
        libraries=libraries,
        library_dirs=library_dirs,
        define_macros=define_macros,
        undef_macros=undef_macros,
        extra_compile_args=extra_compile_args,
    )
]

packages = find_packages()
pymt_components = [
    ("Sedflux3D=pymt_sedflux.lib:Sedflux3D", "meta/Sedflux3D"),
    ("Avulsion=pymt_sedflux.lib:Avulsion", "meta/Avulsion"),
    ("Plume=pymt_sedflux.lib:Plume", "meta/Plume"),
    ("Subside=pymt_sedflux.lib:Subside", "meta/Subside"),
]

setup(
    name="pymt_sedflux",
    author="Eric Hutton",
    description="PyMT plugin sedflux",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)

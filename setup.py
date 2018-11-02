#! /usr/bin/env python
import os
import sys
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points


common_flags = {
    "include_dirs": [np.get_include(), os.path.join(sys.prefix, "include")],
    "library_dirs": [],
    "define_macros": [],
    "undef_macros": [],
    "extra_compile_args": [],
    "language": "c",
}
libraries = []

ext_modules = [
    Extension(
        "pymt_sedflux.lib.sedflux3d",
        ["pymt_sedflux/lib/sedflux3d.pyx"],
        libraries=libraries + ["bmi_sedflux3d"],
        **common_flags,
    ),
    Extension(
        "pymt_sedflux.lib.avulsion",
        ["pymt_sedflux/lib/avulsion.pyx"],
        libraries=libraries + ["bmi_avulsion"],
        **common_flags,
    ),
    Extension(
        "pymt_sedflux.lib.plume",
        ["pymt_sedflux/lib/plume.pyx"],
        libraries=libraries + ["bmi_plume"],
        **common_flags,
    ),
    Extension(
        "pymt_sedflux.lib.subside",
        ["pymt_sedflux/lib/subside.pyx"],
        libraries=libraries + ["bmi_subside"],
        **common_flags,
    ),
]

packages = find_packages()
pymt_components = [
    ("Sedflux3D=pymt_sedflux.bmi:Sedflux3D", "meta/Sedflux3D"),
    ("Avulsion=pymt_sedflux.bmi:Avulsion", "meta/Avulsion"),
    ("Plume=pymt_sedflux.bmi:Plume", "meta/Plume"),
    ("Subside=pymt_sedflux.bmi:Subside", "meta/Subside"),
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

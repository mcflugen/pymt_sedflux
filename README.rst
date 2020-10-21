============
pymt_sedflux
============


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_sedflux-green.svg
        :target: https://anaconda.org/conda-forge/pymt_sedflux

.. image:: https://img.shields.io/travis/pymt-lab/pymt_sedflux.svg
        :target: https://travis-ci.org/pymt-lab/pymt_sedflux

.. image:: https://readthedocs.org/projects/pymt-sedflux/badge/?version=latest
        :target: https://pymt-sedflux.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for sedflux


* Free software: MIT License
* Documentation: https://pymt-sedflux.readthedocs.io.




========= ===================================
Component PyMT
========= ===================================

Avulsion  `from pymt.models import Avulsion`

Plume     `from pymt.models import Plume`

Sedflux3D `from pymt.models import Sedflux3D`

Subside   `from pymt.models import Subside`
========= ===================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-----------------------
Installing pymt_sedflux
-----------------------

Once `pymt` is installed, the dependencies of `pymt_sedflux` can
be installed with:

.. code::

  conda install sedflux

To install `pymt_sedflux`,

.. code::

  conda install pymt_sedflux

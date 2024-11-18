from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        'sealsmodel.seals_cython_functions',
        ['sealsmodel/seals_cython_functions.pyx'],
    )
]

returned = setup(
    install_requires=[
        "gdal",
        "hazelbean",
        "matplotlib",
        "numpy<2",
        "pandas",
        "rasterio",
        "scipy",
    ],
    name='sealsmodel',
    packages=["sealsmodel"],
    include_dirs=[numpy.get_include()],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)

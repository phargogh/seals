from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        'seals.seals_cython_functions',
        ['seals/seals_cython_functions.pyx'],
    )
]

returned = setup(
    install_requires=[
        "gdal",
        "hazelbean",
        "matplotlib",
        "numpy",
        "pandas",
        "rasterio",
        "scipy",
    ],
    name='seals',
    packages=["seals"],
    include_dirs=[numpy.get_include()],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)

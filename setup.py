from setuptools import find_packages, setup
from glob import glob
import os

setup(
    name='teki_rajzolo_pkg',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Martin',
    maintainer_email='langmartin9999@gmail.com',
    description='Teknos formakat rajzol',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'draw_shape = teki_rajzolo_pkg.draw_shape_node:main',
        ],
    },
)

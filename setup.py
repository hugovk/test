#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="test",
    install_requires=['six'],
    tests_require=['mock', 'pytest', 'coverage', 'pep8', 'pyyaml', 'pyflakes'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    packages=find_packages(exclude=('tests*',)),
    license="Apache2"
)

# End of file
